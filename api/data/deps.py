from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import models
from sqlalchemy.orm import Session
from utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from schemas import TokenPayload, SystemUser
from database import get_db


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/login",
    scheme_name="JWT"
)


async def common_parameters_paper(paper_id: int):
    """Define commons parameters

    Args:
        paper_id (int): id of the paper in db

    Returns:
        dict: return paper id
    """
    return {"id": paper_id}


async def common_parameters_author(author_id: int):
    """Define commons parameter

    Args:
        author_id (int): id of an author in db

    Returns:
        dict: return the author id
    """
    return {"id": author_id}


async def common_parameters_batch(offset: int, limit: int):
    """Commons parameter when requesting a batch from db

    Args:
        offset (int): starting point
        limit (int): ending point

    Returns:
        dict: dict of params
    """
    return {"offset": offset,
            "limit": limit}


async def get_secure_paper(
        commons: dict = Depends(common_parameters_paper),
        token: str = Depends(reuseable_oauth),
        db: Session = Depends(get_db)
        ) -> SystemUser:
    """secure the route with JWT auth

    Args:
        commons (dict, optional): params. Defaults to Depends(common_parameters_paper).
        token (str, optional): JWT token. Defaults to Depends(reuseable_oauth).
        db (Session, optional): SQLalchemy instance. Defaults to Depends(get_db).

    Raises:
        HTTPException: 401 non authorized access
        HTTPException: 403 action forbidden
        HTTPException: 404 requested data not found

    Returns:
        SystemUser: data send by the server
    """
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
    data = db.query(models.Paper).filter(
        models.Paper.id == commons['id']).first()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return data


async def get_secure_author(
        commons: dict = Depends(common_parameters_author),
        token: str = Depends(reuseable_oauth),
        db: Session = Depends(get_db)
        ) -> SystemUser:
    """Secure the route with a JWT login

    Args:
        commons (dict, optional): params. Defaults to Depends(common_parameters_author).
        token (str, optional): JWT token. Defaults to Depends(reuseable_oauth).
        db (Session, optional): SQLalchemy instance. Defaults to Depends(get_db).

    Raises:
        HTTPException: 401 login failed
        HTTPException: 403 forbidden action
        HTTPException: 404 data was not found

    Returns:
        SystemUser: response from the server
    """
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
    data = db.query(models.Author).filter(
        models.Author.id == commons['id']).first()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return data


async def get_secure_author_batch(
        commons: dict = Depends(common_parameters_batch),
        token: str = Depends(reuseable_oauth),
        db: Session = Depends(get_db)
        ) -> SystemUser:
    """Secure route with JWT token

    Args:
        commons (dict, optional): params. Defaults to Depends(common_parameters_batch).
        token (str, optional): JWt token. Defaults to Depends(reuseable_oauth).
        db (Session, optional): SQLalchemy instance. Defaults to Depends(get_db).

    Raises:
        HTTPException: 401 login failed
        HTTPException: 403 forbidden action
        HTTPException: 404 data wasn't found

    Returns:
        SystemUser: response from the server
    """
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
    skip, limit = commons['offset'], commons['limit']
    data = db.query(models.Author).offset(skip).limit(limit).all()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return data


async def get_secure_paper_batch(
        commons: dict = Depends(common_parameters_batch),
        token: str = Depends(reuseable_oauth),
        db: Session = Depends(get_db)
        ) -> SystemUser:
    """Secure route with JWT authentification

    Args:
        commons (dict, optional): params. Defaults to Depends(common_parameters_batch).
        token (str, optional): JWT token. Defaults to Depends(reuseable_oauth).
        db (Session, optional): SQLalchemy instance. Defaults to Depends(get_db).

    Raises:
        HTTPException: 401 wrong credidentials
        HTTPException: 403 forbidden action
        HTTPException: 404 data wasn't found

    Returns:
        SystemUser: response from the server
    """
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
    skip, limit = commons['offset'], commons['limit']
    data = db.query(models.Paper).offset(skip).limit(limit).all()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return data
