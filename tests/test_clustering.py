import os
import pandas as pd
import numpy as np
from umap.umap_ import UMAP
from sklearn.cluster import KMeans
from utils import load_embeddings, get_silhouette_scores, get_best_k

ROOT_DIR = os.getcwd()
CLUSTERING_DATA_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'test_data.pkl')
EMBEDDINGS_DATA = os.path.join(ROOT_DIR, 'files', 'pkl', 'test_embeddings.pkl')


def test_files_exist():
    assert os.path.exists(CLUSTERING_DATA_PATH)
    assert os.path.exists(EMBEDDINGS_DATA)


def input_data():
    df = pd.read_pickle(CLUSTERING_DATA_PATH)
    shape = df.shape
    fields = ['paper_id',
              'arxiv_id', 
              'name',
              'article_count',
              'year',
              'title',
              'categories',
              'abstract']
    assert fields == list(df.columns)
    assert shape == (2000, 8)


def test_embeddings():
    df = pd.read_pickle(EMBEDDINGS_DATA)
    assert df.shape == (2000, 1024)
    assert isinstance(df, np.ndarray)

def test_train():
    K = range(3, 15, 1)
    embeddings = load_embeddings(EMBEDDINGS_DATA)
    reducer = UMAP(n_neighbors=20, n_components=3, min_dist=0.01)
    reduce_emb = reducer.fit_transform(embeddings)
    silhouette_scores = get_silhouette_scores(K, reduce_emb)
    max_silhouette = max(silhouette_scores)
    best_k, best_silhouette = get_best_k(K, silhouette_scores)
    best_model = KMeans(n_clusters=best_k,
                        init='k-means++',
                        random_state=42,
                        algorithm='lloyd')
    best_model = best_model.fit(reduce_emb)
    
    df = pd.read_pickle(CLUSTERING_DATA_PATH)
    titles = df['title'].to_list()
    arxiv_ids = df['arxiv_id'].to_list()
    df_cluster = pd.DataFrame({
        "arxiv_id": arxiv_ids,
        "title": titles,
        "x": reduce_emb[:, 0],
        "y": reduce_emb[:, 1],
        "z": reduce_emb[:, 2],
    })
    
    test_arxiv_ids = [
        "1104.1724",
        "2303.04696",
        "1807.04888",
        "1904.08421",
        "1311.1741"
    ]
    
    df_cluster['cluster'] = best_model.predict(df_cluster[['x', 'y', 'z']].to_numpy())
    
    test_cluster = df_cluster[df_cluster['arxiv_id'].isin(test_arxiv_ids)]
    
    assert len(test_cluster['cluster'].unique()) == 1
    assert isinstance(best_model, KMeans)
    assert isinstance(best_k, int)
    assert best_silhouette == max_silhouette