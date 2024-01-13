"""Module that provide some utility functions"""
import os
import re
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

ARXIV_URI = os.getenv("ARXIV")
NIPS_BDD = os.getenv("NIPS_BDD")
OPENAI_KEY = os.getenv('OPENAI_KEY')


def readf(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text


def get_sql_queries(path: str, n: int):
    return text(readf(path).split("\n\n")[n])


def load_arxiv_dataset() -> pd.DataFrame:
    data = []
    cols = [
        "id",
        "authors_parsed",
        "title",
        "abstract",
        "categories",
        "version_1",
    ]

    with open(ARXIV_URI, "r", encoding="utf-8") as jsf:
        for line in jsf:
            doc = json.loads(line)
            list_data = [
                doc["id"],
                doc["authors_parsed"],
                doc["title"],
                doc["abstract"],
                doc["categories"],
                doc["versions"][0]["created"],
            ]
            data.append(list_data)
    return pd.DataFrame(data=data, columns=cols)


def load_arxiv_papers() -> pd.DataFrame:
    data = []
    cols = [
        "title",
        "abstract",
        "version_1",
    ]

    with open(ARXIV_URI, "r", encoding="utf-8") as jsf:
        for line in jsf:
            doc = json.loads(line)
            list_data = [
                doc["title"],
                doc["abstract"],
                doc["versions"][0]["created"]]
            data.append(list_data)
    return pd.DataFrame(data=data, columns=cols)


def format_arxiv_papers(df: pd.DataFrame):
    df["year"] = df["version_1"].map(lambda s: re.findall("\d\d\d\d", s)[0])
    df = df.drop(columns="version_1")
    return df


def load_nips_dataset() -> pd.DataFrame:
    engine = create_engine(f"sqlite:///{NIPS_BDD}")
    query = get_sql_queries("queries.txt", 0)
    with engine.connect() as conn:
        result = conn.execute(query).all()
    return pd.DataFrame(result)


def load_nips_papers() -> pd.DataFrame:
    engine = create_engine(f"sqlite:///{NIPS_BDD}")
    query = get_sql_queries("queries.txt", 1)
    with engine.connect() as conn:
        result = conn.execute(query).all()
    return pd.DataFrame(result)


def format_arxiv_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df["year"] = df["version_1"].map(lambda strg: strg.split()[3])
    df["authors"] = df["authors_parsed"].apply(
        lambda ls: [" ".join(name).strip() for name in ls]
    )
    df = df.drop(columns=["authors_parsed", "categories", "version_1"])
    return df


client = OpenAI(api_key=OPENAI_KEY)


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(
        input=[text],
        model=model).data[0].embedding
