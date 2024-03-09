import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # kept secret
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')  # kept secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """Hashed a raw_password with the hs256 algorithm

    Args:
        password (str): raw_password

    Returns:
        str: hashed password
    """
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify the correspondance between a raw_password and a hashed password

    Args:
        password (str): raw_password
        hashed_pass (str): hashed password

    Returns:
        bool: true if there is a match, false otherwise
    """
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any],
                        expires_delta: int = None) -> str:
    """Handle the creation of an JWT token for user's identification

    Args:
        subject (Union[str, Any]): string used for encoding
        expires_delta (int, optional): token expiration date. Defaults to None.

    Returns:
        str: encoded token
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any],
                         expires_delta: int = None) -> str:
    """Create a refresh token

    Args:
        subject (Union[str, Any]): string used for encoding
        expires_delta (int, optional): refresh token expiration date. Defaults to None.

    Returns:
        str: refresh token
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt