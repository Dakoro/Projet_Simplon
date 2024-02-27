import os
import pickle
import torch
import pandas as pd
from transformers import AutoModelForMaskedLM, AutoTokenizer
from langchain_community.document_loaders import DataFrameLoader
from qdrant_client import QdrantClient, models
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = 'hybrid_search'
OPENAI_KEY = os.getenv('OPENAI_KEY')
model_id = "naver/splade-cocondenser-ensembledistil"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

openai_client = OpenAI(api_key=OPENAI_KEY)


def compute_sparse_vector(text):
    """
    Computes a vector from logits and attention mask
    using ReLU, log, and max operations.
    """
    tokens = tokenizer(text, return_tensors="pt")
    output = model(**tokens)
    logits, attention_mask = output.logits, tokens.attention_mask
    relu_log = torch.log(1 + torch.relu(logits))
    weighted_log = relu_log * attention_mask.unsqueeze(-1)
    max_val, _ = torch.max(weighted_log, dim=1)
    vec = max_val.squeeze()

    return vec, tokens


def qdrant_hybrid_search(client: QdrantClient, query_text, emb_model):
    vec, _ = compute_sparse_vector(query_text)
    cols = vec.nonzero().squeeze().cpu().tolist()
    weights = vec[cols].cpu().tolist()
    sparse_dict = dict(zip(cols, weights))
    query_indices, query_values = (list(sparse_dict.keys()),
                                   list(sparse_dict.values()))
    query_dense_vector = emb_model.encode(query_text,
                                          normalize_embeddings=True)
    result = client.search_batch(
        collection_name=COLLECTION_NAME,
        requests=[
            models.SearchRequest(
                vector=models.NamedVector(
                    name="text-dense",
                    vector=query_dense_vector,
                ),
                limit=5,
            ),
            models.SearchRequest(
                vector=models.NamedSparseVector(
                    name="text-sparse",
                    vector=models.SparseVector(
                        indices=query_indices,
                        values=query_values,
                    ),
                ),
                limit=5,
            ),
        ],
    )

    return result


def retrieve_documents(result, data):
    list_idx = []
    for lst in result:
        for r in lst:
            idx = (r.model_dump()['id'], r.model_dump()['score'])
            list_idx.append(idx)
    result_query = []
    for idx, d in enumerate(data, start=1):
        for vec_id, _ in list_idx:
            if idx == vec_id or 2*idx == vec_id:
                result_query.append(d)
    return result_query


def api_call(messages, model):
    return openai_client.chat.completions.create(
        model=model,
        messages=messages,
        stop=["\n\n"],
        max_tokens=100,
        temperature=0.0,
    )


def get_data(fp):
    df = pd.read_csv(fp)
    df = df[['title', 'name', 'year', 'abstract']]
    return DataFrameLoader(df, page_content_column='abstract').load()


def get_answer(client, query, embeddings, data):
    result_search = qdrant_hybrid_search(client, query, embeddings)
    relevant_docs = retrieve_documents(result_search, data)
    context = '\n'.join([d.page_content for d in relevant_docs])
    print(relevant_docs)
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""Answer the following Question
                                by reading the Context
                                first. Then your task is to construct an answer
                                based on what you understood.
                                If you don't know the answer,
                                say 'I don't know'.
            Question: {query}\n\n
            Context: {context}\n\n
            Answer:\n""",
            },
        ]
    response = {
        "openai": api_call(messages=messages, model="gpt-3.5-turbo-0125"),
        "relevants_docs": relevant_docs
    }
    return response


def load_pickle(path: str):
    with open(path, 'rb') as pklf:
        data = pickle.load(pklf)
    return data
