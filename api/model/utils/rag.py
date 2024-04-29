import os
import pickle
import pandas as pd
from pathlib import Path
from langchain_community.document_loaders import DataFrameLoader
from langchain.vectorstores.qdrant import Qdrant
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(os.getcwd()).parent.parent
OPENAI_KEY = os.getenv('OPENAI_KEY')
QDRANT_URI = os.getenv('QDRANT_URI')
COLLECTION_NAME = 'arxiv'

openai_client = OpenAI(api_key=OPENAI_KEY)

def init_retriever(client, embeddings, k=10):
    qdrant = Qdrant(
        client=client,
        embeddings=embeddings,
        collection_name='abstracts'
    )
    return qdrant.as_retriever(search_type="mmr", search_kwargs={'k': k})


def api_call(messages, model):
    return openai_client.chat.completions.create(
        model=model,
        messages=messages,
        stop=["\n\n"],
        max_tokens=100,
        temperature=0.0,
    )


def get_data(fp):
    df = pd.read_pickle(fp)
    df = df[['title', 'name', 'year', 'abstract']]
    return DataFrameLoader(df, page_content_column='abstract').load()


def get_answer(retriever, query):
    relevant_docs = retriever.get_relevant_documents(query)
    context = '\n'.join([d.page_content for d in relevant_docs])
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
