from datetime import datetime
from typing import Annotated
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


async def common_parameters(paper_id: int):
    return {"id": paper_id}


async def get_secure_paper(
        commons: dict = Depends(common_parameters),
        token: str = Depends(reuseable_oauth),
        db: Session = Depends(get_db),
        ) -> SystemUser:
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
    print()
    data = db.query(models.Paper).filter(
        models.Paper.id == commons['paper_id']).first()

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find data",
        )

    return data
