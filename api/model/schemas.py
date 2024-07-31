from uuid import UUID
from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """Validation schema for JWT token

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    """Validation schema for the token payload

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    """Validation schema for user authentification

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    username: str = Field(..., description="username")
    password: str = Field(...,
                          min_length=5,
                          max_length=24,
                          description="user password")


class UserOut(BaseModel):
    """Validation schema for user logout

    Args:
        BaseModel (_type_): _description_
    """
    id: UUID
    username: str


class SystemUser(UserOut):
    password: str
