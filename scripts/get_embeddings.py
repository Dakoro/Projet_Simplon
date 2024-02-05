from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle

COLS = ['paper_id',
        'name',
        'article_count',
        'year',
        'title',
        'source',
        'abstract']


def main():
    df = pd.read_csv("/home/dakoro/Projet_Simplon/sample.csv", names=COLS)
    model = SentenceTransformer(model_name_or_path='BAAI/bge-large-en-v1.5')
    df['embeddings'] = df['abstract'].map(lambda s: model.encode(s))
    df.to_pickle("../sample_with_embeddings.pkl",
                 protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
