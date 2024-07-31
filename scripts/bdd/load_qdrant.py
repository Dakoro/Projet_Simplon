import os
import pickle
import pandas as pd
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.document_loaders.dataframe import DataFrameLoader
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain.vectorstores.qdrant import Qdrant

ROOT_DIR = os.getcwd()
CACHE_DIR = os.path.join(ROOT_DIR, '.cache_emb')
SAMPLE_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'sample.pkl')
EMB_MODEL = SentenceTransformerEmbeddings(model_name='BAAI/bge-large-en-v1.5')
CHUNKS_DIR = os.path.join(ROOT_DIR, 'pdfs', 'chunks')
CACHE_EMB = CacheBackedEmbeddings.from_bytes_store(
    EMB_MODEL, LocalFileStore(CACHE_DIR), namespace=EMB_MODEL.model_name
)

def read_pkl_dir(pkl_dir: str):
    data = []
    fnames = sorted([fname for fname in os.listdir(pkl_dir) if fname.endswith('.pkl')],
                key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].split('_')[1]))
    list_fps = [os.path.join(pkl_dir, fn) for fn in fnames]
    for fp in list_fps:
        with open(fp, 'rb') as pklf:
            data += pickle.load(pklf)
    return data


def load_abstracts():
    df = pd.read_pickle(SAMPLE_PATH)
    loader_df = DataFrameLoader(df, page_content_column='abstract')
    docs = loader_df.load()
    Qdrant.from_documents(
        docs,
        CACHE_EMB,
        host='localhost',
        port='6334',
        collection_name='abstracts',
        prefer_grpc=True,
        force_recreate=True)


def load_fulltexts():
    docs = read_pkl_dir(CHUNKS_DIR)
    docs = [doc for doc in docs if len(doc.page_content.split()) > 20]
    Qdrant.from_documents(
        docs,
        CACHE_EMB,
        host='localhost',
        port='6334',
        collection_name='Papers',
        prefer_grpc=True,
        force_recreate=True)
    
    

def main():
    load_abstracts()
    load_fulltexts()


if __name__ == '__main__':
    main()