import os
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import UserOut, UserAuth, TokenSchema
from deps import (
    get_secure_topic,
    get_secure_rag,
    get_secure_topic_over_time,
    get_secure_cluster,
)
from utils.auth import (
    get_hashed_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from uuid import uuid4

app = FastAPI(debug=True)

ROOT_DIR = Path(os.getcwd()).parent.parent
EMB_MODEL = SentenceTransformer("BAAI/bge-large-en-v1.5")
BERTOPIC_MODEL_PATH = os.path.join(ROOT_DIR, "models", "bertopic")


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")


@app.post("/api/inference/bertopic")
async def get_topic_model(abstract=Depends(get_secure_topic)):
    return abstract


@app.get("/api/inference/bertopic/topic_over_time")
async def get_topic_over(fig: str = Depends(get_secure_topic_over_time)):
    return fig


@app.post("/api/inference/rag")
async def rag(answer: str = Depends(get_secure_rag)):
    return answer


@app.get("/api/clustering")
async def clustering(data: pd.DataFrame = Depends(get_secure_cluster)):
    return data.to_dict()


@app.post("/api/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth, db: Session = Depends(get_db)):
    # querying database to check if user already exist
    user = db.query(models.User).filter(models.User.username == data.username).first()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exist",
        )
    user = {
        "username": data.username,
        "password": get_hashed_password(data.password),
        "id": str(uuid4()),
    }

    db_user = models.User(
        id=user["id"], username=user["username"], password=user["password"]
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user


@app.post(
    "/api/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(models.User).filter(models.User.username == form_data.username).first()
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
    }
