import pickle


def load_embeddings():
    with open('embeddings.pkl', 'rb') as pklf:
        embeddings = pickle.load(pklf)
    return embeddings
