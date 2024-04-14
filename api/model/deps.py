import os
from pathlib import Path
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from bertopic import BERTopic
from qdrant_client import QdrantClient
from jose import jwt
from pydantic import ValidationError
from sentence_transformers import SentenceTransformer
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from qdrant_client.qdrant_client import QdrantClient
from schemas import TokenPayload
from utils.rag import get_answer, get_data, load_pickle, init_retriever
from utils.clustering import get_cluster_data
from utils.auth import (
    ALGORITHM,
    JWT_SECRET_KEY
)

ROOT_DIR = Path(os.getcwd()).parent.parent
BERTOPIC_MODEL_PATH = os.path.join(ROOT_DIR, 'models', 'bertopic')
EMB_MODEL = SentenceTransformer('BAAI/bge-large-en-v1.5')
LANG_EMB_MODEL = SentenceTransformerEmbeddings(model_name='BAAI/bge-large-en-v1.5')
TOPIC_OVER_TIME_PATH = os.path.join(ROOT_DIR, 'files', 'pkl', 'topic_over_time.pkl')
QDRANT_URI = os.getenv('QDRANT_URI')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

client = QdrantClient(
    url=QDRANT_URI,
    api_key=QDRANT_API_KEY,
    prefer_grpc=True
)

qdrant_retriever = init_retriever(client, LANG_EMB_MODEL, k=10)

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/login",
    scheme_name="JWT"
)


async def common_parameters(abstract: str):
    return {"abstract": abstract}


async def rag_params(question: str):
    return {"question": question}


async def get_secure_topic(
        commons: dict = Depends(common_parameters),
        token: str = Depends(reuseable_oauth),
        ):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not isinstance(commons['abstract'], str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="parameter must be a string",
        )
    model = BERTopic().load(BERTOPIC_MODEL_PATH,
                            embedding_model=EMB_MODEL)
    topic, _ = model.transform([commons['abstract']])
    result = model.get_topic(topic=topic[0], full=True)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't infer topic",
        )
    return result


async def get_secure_rag(
        rag_params: dict = Depends(rag_params),
        token: str = Depends(reuseable_oauth),
        ):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    question = rag_params['question']
    answer = get_answer(qdrant_retriever, question)

    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return answer


async def get_secure_topic_over_time(
        token: str = Depends(reuseable_oauth),
        ):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    model = BERTopic().load(BERTOPIC_MODEL_PATH,
                            embedding_model=EMB_MODEL)
    path = TOPIC_OVER_TIME_PATH
    topic_over_time = load_pickle(path)
    fig = model.visualize_topics_over_time(topic_over_time,
                                           top_n_topics=20,
                                           width=900,
                                           height=500)

    if fig is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return fig.to_html(full_html=False)


async def get_secure_cluster(
        token: str = Depends(reuseable_oauth),
        ):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    cluster_data = get_cluster_data()

    if cluster_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )
    return cluster_data
