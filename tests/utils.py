import pickle
from dotenv import load_dotenv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
load_dotenv()

def load_embeddings(path: str):
    with open(path, 'rb') as pklf:
        embeddings = pickle.load(pklf)
    return embeddings

def get_silhouette_scores(K: list[int], reduce_emb):
    silhouette_scores = []
    for k in K:
        km = KMeans(n_clusters=k,
                    init='k-means++',
                    random_state=42,
                    algorithm='lloyd')
        km = km.fit(reduce_emb)
        labels = km.labels_
        score = silhouette_score(reduce_emb, labels)
        silhouette_scores.append(score)
    return silhouette_scores


def get_best_k(K, silhouette_scores):
    best_score = max(silhouette_scores)
    for k, score in zip(K, silhouette_scores):
        if score == best_score:
            return (k, score)