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
    df = df.iloc[1:]
    model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    docs = df['abstract'].to_list()
    embeddings = model.encode(docs, show_progress_bar=True)

    with open("./embeddings.pkl", 'wb') as pklf:
        pickle.dump(embeddings, pklf)


if __name__ == "__main__":
    main()
