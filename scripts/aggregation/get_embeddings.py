import os
import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

SAMPLE_PATH = os.path.join(os.getcwd(), 'files', 'pkl', 'sample.pkl')
EMBEDDINGS_PATH = os.path.join(os.getcwd(), 'files', 'pkl', 'embeddings.pkl')

def main():
    df = pd.read_pickle(SAMPLE_PATH)
    print(df.columns)
    model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    docs = df['abstract'].to_list()
    embeddings = model.encode(docs, show_progress_bar=True)

    with open(EMBEDDINGS_PATH, 'wb') as pklf:
        pickle.dump(embeddings, pklf)


if __name__ == "__main__":
    main()
