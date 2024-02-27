import os
import mlflow
import joblib
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = os.getenv('ROOT_DIR')
MLFLOW_URI = os.getenv('MLFLOW_URI')
mlflow.set_tracking_uri(uri=MLFLOW_URI)
logged_model = 'runs:/f8cd5acc46b04985afb5a99f03144bad/KMeans_model'
loaded_model = mlflow.pyfunc.load_model(logged_model)


def get_cluster_data(data):
    path = os.path.join(ROOT_DIR, 'files', 'pkl', 'umap_proj.pkl')
    with open(path, 'rb') as pklf:
        reduce_emb = joblib.load(pklf)
    y = loaded_model.predict(reduce_emb)
    df = pd.DataFrame({
        "proj_x": reduce_emb[:, 0],
        "proj_y": reduce_emb[:, 1],
        "proj_z": reduce_emb[:, 2],
        "cluster": y
    })
    return df
