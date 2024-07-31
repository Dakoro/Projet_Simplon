import os
import mlflow
import pickle
import pandas as pd
from mlflow.models import infer_signature
from dotenv import load_dotenv
from utils import load_embeddings
from umap.umap_ import UMAP
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
load_dotenv()

ROOT_DIR = os.getcwd()
MFLOW_URI = os.getenv('MLFLOW_TRACKING_URI')
EMB_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'embeddings.pkl')
SAMPLE_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'sample.pkl')

mlflow.set_tracking_uri(uri=MFLOW_URI)
mlflow.set_experiment("Clustering")


def get_silhouette_scores(K: list[int], reduce_emb):
    silhouette_scores = []
    for k in K:
        with mlflow.start_run(run_name=f'KMeans_{k}'):
            km = KMeans(n_clusters=k,
                        init='k-means++',
                        random_state=42,
                        algorithm='lloyd')
            mlflow.log_params(km.get_params())
            km = km.fit(reduce_emb)
            labels = km.labels_
            score = silhouette_score(reduce_emb, labels)
            mlflow.log_metric("silhouette", score)
            silhouette_scores.append(score)
    return silhouette_scores


def get_best_k(K, silhouette_scores):
    best_score = max(silhouette_scores)
    for k, score in zip(K, silhouette_scores):
        if score == best_score:
            return k


def main():
    K = range(3, 15, 1)
    embeddings = load_embeddings(EMB_PATH)
    reducer = UMAP(n_neighbors=20, n_components=3, min_dist=0.01)
    reduce_emb = reducer.fit_transform(embeddings)
    silhouette_scores = get_silhouette_scores(K, reduce_emb)
    best_k = get_best_k(K, silhouette_scores)
    best_model = KMeans(n_clusters=best_k,
                        init='k-means++',
                        random_state=42,
                        algorithm='lloyd')
    best_model = best_model.fit(reduce_emb)
    signature = infer_signature(reduce_emb, best_model.predict(reduce_emb))
    
    # start mlflow run
    with mlflow.start_run(run_name='best_KMeans'):
        mlflow.log_params(best_model.get_params())
        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="KMeans_model",
            registered_model_name="KMeans_model",
            signature=signature)
    
    df = pd.read_pickle(SAMPLE_PATH)
    titles = df['title'].to_list()
    arxiv_ids = df['arxiv_id'].to_list()
    df_cluster = pd.DataFrame({
        "arxiv_id": arxiv_ids,
        "title": titles,
        "x": reduce_emb[:, 0],
        "y": reduce_emb[:, 1],
        "z": reduce_emb[:, 2],
    })
    reducer_path = os.path.join(ROOT_DIR,
                                'files',
                                'pkl',
                                'cluster_data.pkl')
    df_cluster.to_pickle(reducer_path, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
