import os
import pickle
from qdrant_client import QdrantClient, models
from langchain.vectorstores.qdrant import Qdrant
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = os.getcwd()
CHUNKS_DIR = os.path.join(ROOT_DIR, 'pdfs', 'chunks')



def read_pickle(fp: str):
    with open(fp, 'rb') as pklf:
        data = pickle.load(pklf)
    return data


def read_pkl_dir(pkl_dir: str):
    data = []
    fnames = sorted([fname for fname in os.listdir(pkl_dir) if fname.endswith('.pkl')],
                key=lambda f: int(f.rsplit(os.path.extsep, 1)[0].split('_')[1]))
    list_fps = [os.path.join(pkl_dir, fn) for fn in fnames]
    for fp in list_fps:
        data += read_pickle(fp)
    return data


def load_cached_embedder(path: str, model: SentenceTransformerEmbeddings):
    store = LocalFileStore(path)
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        model,
        store,
        namespace=model.model_name
    )
    return cached_embedder


def recreate_collection(collection_name):
    client = QdrantClient(host='localhost',
                          port=6333)
    print('init client')
    if client.collection_exists(collection_name=f"{collection_name}"):
        print('recreate collection')
        client.delete_collection(collection_name=f"{collection_name}")
    client.create_collection(
        collection_name=f"{collection_name}",
        vectors_config=models.VectorParams(size=1024,
                                           distance=models.Distance.COSINE,
                                           on_disk=True),
        optimizers_config=models.OptimizersConfigDiff(memmap_threshold=20000),
    )
    
    print('collection create')
    
    

def main():
    model = SentenceTransformerEmbeddings(model_name='BAAI/bge-large-en-v1.5')
    embeddings = load_cached_embedder('.cache_emb/', model)
    print(model.model_name)
    docs = read_pkl_dir(CHUNKS_DIR)
    filtered_docs = [doc for doc in docs if len(doc.page_content.split()) > 20]
    print(f"Number of docs: {len(filtered_docs)}")
    recreate_collection("Papers")
    Qdrant.from_documents(
        filtered_docs,
        embeddings,
        host='localhost',
        port=6334,
        prefer_grpc=True,
        collection_name="Papers"
    )


if __name__ == '__main__':
    main()