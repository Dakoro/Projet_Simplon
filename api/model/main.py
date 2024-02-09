from fastapi import FastAPI
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from utils import get_answer

app = FastAPI(debug=True)

BERTOPIC_MODEL_PATH = "/home/dakoro/Projet_Simplon/models/bertopic"


@app.post("/api/inference/bertopic")
async def load_topic_model(abstract: str):
    embedding_model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    model = BERTopic().load(BERTOPIC_MODEL_PATH,
                            embedding_model=embedding_model)
    topic, _ = model.transform([abstract])
    result = model.get_topic(topic=topic[0], full=True)
    return result


@app.post("/api/inference/rag")
async def rag(question: str):
    answer = get_answer(question)
    return answer
