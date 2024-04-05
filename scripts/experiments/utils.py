import pickle

def load_embeddings(path: str):
    with open(path, 'rb') as pklf:
        embeddings = pickle.load(pklf)
    return embeddings
