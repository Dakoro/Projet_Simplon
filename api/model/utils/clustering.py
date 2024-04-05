import os
import mlflow
import joblib
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = Path(os.getcwd()).parent.parent
MLFLOW_URI = os.getenv('MLFLOW_URI')
KMEANS_URI = os.getenv('KMEANS_RUN_URI')

mlflow.set_tracking_uri(uri=MLFLOW_URI)
loaded_model = mlflow.pyfunc.load_model(KMEANS_URI)


def get_cluster_data():
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
