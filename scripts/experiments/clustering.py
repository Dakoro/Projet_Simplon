import os
import mlflow
import joblib
from mlflow.models import infer_signature
from dotenv import load_dotenv
from utils import load_embeddings
from umap.umap_ import UMAP
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
load_dotenv()

ROOT_DIR = os.getenv('ROOT_DIR')
MFLOW_URI = os.getenv('MLFLOW_URI')

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
    K = range(2, 10, 1)
    embeddings = load_embeddings()
    reducer = UMAP(n_neighbors=20, n_components=5, min_dist=0.01)
    reduce_emb = reducer.fit_transform(embeddings)
    silhouette_scores = get_silhouette_scores(K, reduce_emb)
    best_k = get_best_k(K, silhouette_scores)
    best_model = KMeans(n_clusters=best_k,
                        init='k-means++',
                        random_state=42,
                        algorithm='lloyd')
    best_model = best_model.fit(reduce_emb)
    signature = infer_signature(reduce_emb, best_model.predict(reduce_emb))
    with mlflow.start_run(run_name='best_KMeans'):
        mlflow.log_params(best_model.get_params())
        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="KMeans_model",
            signature=signature)
        reducer_path = os.path.join(ROOT_DIR,
                                    'files',
                                    'pkl',
                                    'umap_proj.pkl')
        with open(reducer_path, "wb") as f:
            joblib.dump(reduce_emb, f)


if __name__ == '__main__':
    main()
