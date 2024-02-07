from fastapi import FastAPI
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from utils import get_answer

app = FastAPI(debug=True)

BERTOPIC_MODEL_PATH = "/home/dakoro/Projet_Simplon/models/bertopic"


@app.get("/api/inference/bertopic")
async def load_topic_model():
    abstract = ["""
    The atom localization of a V-type atomic system is discussed by the
    detunings associated with the probe and the two orthogonal standing-wave
    fields, and by the spontaneously generated coherence (SGC). Within the
    half-wavelength domain in the 2-dimensional(2-D) plane, the atom
    localization depicted by the probe dual absorption peaks is achieved when
    the detunings are tuned. However, the dual peaks change into single-peak
    when the SGC arises. The single-peak 2-D localization demonstrated
    the advantage for atom localization achieved by the flexible
    manipulating parameters in our scheme.
    """]
    embedding_model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    model = BERTopic().load(BERTOPIC_MODEL_PATH,
                            embedding_model=embedding_model)
    topic, _ = model.transform(abstract)
    result = model.get_topic(topic=topic[0], full=True)
    return result


@app.get("/api/inference/rag")
async def rag():
    question = "What is gauge theory"
    answer = get_answer(question)
    return answer
