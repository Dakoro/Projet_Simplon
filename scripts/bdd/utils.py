"""Module that provide some utility functions"""
import os
import re
import json
import arxiv
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import Tag
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sqlalchemy import create_engine, text

load_dotenv()

ROOT_DIR = os.getcwd()
ARXIV_URI = os.path.join(ROOT_DIR, os.getenv("ARXIV"))
NIPS_BDD = os.path.join(ROOT_DIR, os.getenv("NIPS_BDD"))


def readf(path: str) -> str:
    """
    Read a text file

    Args:
        path (str): file path

    Returns:
        str: text in the file
    """
    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text


def get_sql_queries(path: str, n: int):
    """Parse the queries.txt file

    Args:
        path (str): file path
        n (int): number of the request

    Returns:
        str: sql query in text format
    """
    return text(readf(path).split("\n\n")[n])


def load_arxiv_dataset(limit: int = None) -> pd.DataFrame:
    """Load arxiv dataset from the json file

    Args:
        limit (int): set a limit of rows to extract

    Returns:
        pd.DataFrame: Daframe with the data
    """
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
        for idx, line in enumerate(jsf, start=1):
            if idx == limit:
                break
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


def load_arxiv_papers(limit: int = None) -> pd.DataFrame:
    """Load arxiv papers from the arxiv json    

    Args:
        limit (int, optional): set optional limit

    Returns:
        pd.DataFrame: ouput df
    """
    data = []
    cols = [
        "arxiv_id",
        "title",
        "abstract",
        "version_1",
        "categories"
    ]

    with open(ARXIV_URI, "r", encoding="utf-8") as jsf:
        for idx, line in enumerate(jsf, start=1):
            if idx == limit:
                break
            doc = json.loads(line)
            list_data = [
                doc['id'],
                doc["title"],
                doc["abstract"],
                doc["versions"][0]["created"],
                doc['categories']]
            data.append(list_data)
    return pd.DataFrame(data=data, columns=cols)


def format_arxiv_papers(df: pd.DataFrame):
    """Format arxiv dataset

    Args:
        df (pd.DataFrame): input df

    Returns:
        df: formated datframe
    """
    df["year"] = df["version_1"].map(
        lambda s: re.findall("\d\d\d\d", s)[0])
    df = df.drop(columns="version_1")
    return df


def load_nips_dataset() -> pd.DataFrame:
    """Load NIPS dataset

    Returns:
        pd.DataFrame: output dataframe
    """
    engine = create_engine(f"sqlite:///{NIPS_BDD}")
    query = get_sql_queries(os.path.join(os.getcwd(), 'queries.txt'), 0)
    with engine.connect() as conn:
        result = conn.execute(query).all()
    return pd.DataFrame(result)


def load_nips_papers() -> pd.DataFrame:
    """Load table from the NIPS db

    Returns:
        pd.DataFrame: output df
    """
    engine = create_engine(f"sqlite:///{NIPS_BDD}")
    query = get_sql_queries(os.path.join(os.getcwd(), 'queries.txt'), 1)
    with engine.connect() as conn:
        result = conn.execute(query).all()
    return pd.DataFrame(result)


def format_arxiv_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """format arxiv dataset

    Args:
        df (pd.DataFrame): input df

    Returns:
        pd.DataFrame: formated output df
    """
    df["year"] = df["version_1"].map(lambda strg: strg.split()[3])
    df["authors"] = df["authors_parsed"].apply(
        lambda ls: [" ".join(name).strip() for name in ls]
    )
    df = df.drop(columns=["authors_parsed", "categories", "version_1"])
    return df


def request_arxiv() -> pd.DataFrame:
    """handle request to the arxiv api

    Returns:
        pd.DataFrame: data stored in a df
    """
    arxiv_client = arxiv.Client()
    arxiv_search = arxiv.Search(
        query='quantum',
        max_results=10,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = {
        "arxiv_id": [],
        "title": [],
        "year": [],
        "authors": [],
        "categories": [],
        "abstract": []
    }

    for result in arxiv_client.results(arxiv_search):
        results['arxiv_id'].append(result.entry_id.split('/')[-1])
        results['title'].append(result.title)
        results['year'].append(result.published)
        results['authors'].append(", ".join([str(a) for a in result.authors]))
        results["categories"].append(result.primary_category)
        results['abstract'].append(result.summary)

    df = pd.DataFrame.from_dict(results)
    df = df.rename(columns={"authors": "author"})
    return df


def parse_title(title_tag: Tag) -> str:
    """Parse the title in a html file

    Args:
        title_tag (Tag): title tag 

    Returns:
        str: title in a string format
    """
    tag_split = title_tag.string.split()
    title = ' '.join(tag_split[1:])
    return title


def extract_year(year_string: str):
    """Regular expression to extract the year

    Args:
        year_string (str): input string

    Returns:
        str: ouput string
    """
    pattern = "\d\d\d\d"
    return re.findall(pattern, year_string)[-1]


def get_scraping():
    """Scrape an html file and extract data

    Returns:
        pd.DataFrame: ouput df
    """
    path = os.path.join(ROOT_DIR, "data_source", "doc_scraping.html")
    with open(path, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, features="html.parser")
    
    title_tag = soup.find('title')
    title = parse_title(title_tag)
    
    arxiv_id = re.findall(r'\[(.*?)\]', title_tag.text)
    arxiv_id = arxiv_id[0]

    abstract_tag = soup.find("div", {"class": "ltx_abstract"})
    abstract = abstract_tag.find("p").string
    
    date_tag = soup.find("div", {"class": "ltx_dates"})
    year = extract_year(date_tag.string)

    author_tag = soup.find("span", {"class": "ltx_personname"})
    author = re.sub('\n', '', author_tag.text)

    df = pd.DataFrame({
        "arxiv_id": [arxiv_id],
        "title": [title],
        "year": [year],
        "author": [author],
        "abstract": [abstract]
    })
    return df


def get_mongo():
    """Extract the data from a Mongo db instance

    Returns:
        pd.DataFrame: ouput df
    """
    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_MDP')
    uri = f"mongodb+srv://{username}:{password}@arxiv.rpllyly.mongodb.net/?retryWrites=true&w=majority&appName=Arxiv"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        # client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client['Arxiv']
        collection = db['Articles']
        docs = collection.find()
        df = pd.DataFrame(docs)
        return df.drop(columns='_id')
    except Exception as e:
        print(e)
