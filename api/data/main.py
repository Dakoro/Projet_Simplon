from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from deps import (
    get_secure_paper,
    get_secure_author,
    get_secure_author_batch,
    get_secure_paper_batch
    )
import models
from schemas import UserOut, UserAuth, TokenSchema
from utils import (
    get_hashed_password,
    verify_password,
    create_access_token,
    create_refresh_token
    )
from uuid import uuid4

app = FastAPI(debug=True)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.get("/api/papers/")
async def get_papers_batch(data: dict = Depends(get_secure_paper_batch)):
    return data


@app.get("/api/paper/")
async def get_paper(data: dict = Depends(get_secure_paper)):
    return data


@app.get("/api/authors/")
async def get_authors_batch(data: Session = Depends(get_secure_author_batch)):
    return data


@app.get("/api/author/")
async def get_author(data: dict = Depends(get_secure_author)):
    return data


@app.post('/api/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth, db: Session = Depends(get_db)):
    # querying database to check if user already exist
    user = db.query(models.User).filter(
        models.User.email == data.email).first()
    print(user)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }

    db_user = models.User(id=user['id'],
                          email=user['email'],
                          password=user['password'])
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user


@app.post('/api/login',
          summary="Create access and refresh tokens for user",
          response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }
