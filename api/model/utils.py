import os
from operator import itemgetter
import chromadb
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings
)
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import format_document
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import get_buffer_string
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = os.getenv('OPENAI_KEY')

_template = """Given the following conversation and a follow up question,
rephrase the follow up question to be a standalone question,
in its original language.

    Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """Answer the question based on the following context and
your knowledge. The context is more important than your knowledge:
{context}

Question: {question}
"""
ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(
    template="{page_content}")


def _combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


def init_retriever(
        path: str,
        embedding_func: SentenceTransformerEmbeddings,
        search_mode: str,
        search_kwargs: dict):
    client = chromadb.PersistentClient(path)
    vec = Chroma(client=client, embedding_function=embedding_func)
    retriever = vec.as_retriever(
        search_type=search_mode,
        search_kwargs=search_kwargs)
    return retriever


def init_rag():
    embedding_func = SentenceTransformerEmbeddings(
        model_name='BAAI/bge-large-en-v1.5')
    retriever = init_retriever(
        path="/home/dakoro/Projet_Simplon/chroma_storage",
        embedding_func=embedding_func,
        search_mode="mmr",
        search_kwargs={"k": 10}
    )

    memory = ConversationBufferMemory(
        return_messages=True, output_key="answer", input_key="question"
    )

    loaded_memory = RunnablePassthrough.assign(
        chat_history=RunnableLambda(
            memory.load_memory_variables) | itemgetter("history"),
    )
    # Now we calculate the standalone question
    standalone_question = {
        "standalone_question": {
            "question": lambda x: x["question"],
            "chat_history": lambda x: get_buffer_string(x["chat_history"]),
        }
        | CONDENSE_QUESTION_PROMPT
        | ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY)
        | StrOutputParser(),
    }
    # Now we retrieve the documents
    retrieved_documents = {
        "docs": itemgetter("standalone_question") | retriever,
        "question": lambda x: x["standalone_question"],
    }
    # Now we construct the inputs for the final prompt
    final_inputs = {
        "context": lambda x: _combine_documents(x["docs"]),
        "question": itemgetter("question"),
    }
    # And finally, we do the part that returns the answers
    answer = {
        "answer": final_inputs | ANSWER_PROMPT | ChatOpenAI(
            api_key=OPENAI_API_KEY),
        "docs": itemgetter("docs"),
    }
    # And now we put it all together!
    final_chain = loaded_memory | standalone_question | retrieved_documents | answer
    return final_chain


def get_answer(question: str):
    response = {}
    response['question'] = question
    chain = init_rag()
    return chain.invoke(response)
