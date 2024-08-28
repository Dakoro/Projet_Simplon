import os
import mlflow
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = Path(os.getcwd()).parent.parent
MLFLOW_URI = os.getenv('MLFLOW_TRACKING_URI')

mlflow.set_tracking_uri(uri=MLFLOW_URI)
model_name = "KMeans_model"
model_version = 1

loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")


def get_cluster_data():
    path = os.path.join(ROOT_DIR, 'files', 'pkl', 'clustering_data.pkl')
    df = pd.read_pickle(path)
    reduce_emb = df[['x', 'y', "z"]].to_numpy()
    df['cluster'] = loaded_model.predict(reduce_emb)
    return df
