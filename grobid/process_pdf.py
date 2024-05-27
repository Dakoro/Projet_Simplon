import os
import pickle
from langchain_community.document_loaders.generic import GenericLoader
from utils import CustomGrobidParser


ROOT_DIR = os.getcwd()
PDF_DIR = os.path.join(ROOT_DIR, 'pdfs')
CHUNKS_DIR = os.path.join(PDF_DIR, 'chunks')


def write_pickle(obj, path):
    with open(path, 'wb') as pklf:
        pickle.dump(obj, pklf)

def parsing_grobid(list_pdfs: list[str]):
    docs = []
    for fp in list_pdfs:
        try:
            loader = GenericLoader.from_filesystem(
                fp,
                parser=CustomGrobidParser(segment_sentences=False),
            )
            docs += loader.load()
        except Exception:
            continue
    return docs


def main():
    list_pdfs = [os.path.join(PDF_DIR, fn) for fn in os.listdir(PDF_DIR)]
    for i in range(0, len(list_pdfs), 100):
        pickle_path = os.path.join(CHUNKS_DIR, f"documents_{i}.pkl")
        if os.path.exists(pickle_path):
            print(f"{pickle_path} already exists")
            continue
        subpart = list_pdfs[i:i+100]
        docs = parsing_grobid(subpart)
        write_pickle(docs, pickle_path)


if __name__ == '__main__':
    main()
    