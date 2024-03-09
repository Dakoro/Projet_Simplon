from uuid import UUID
from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """Basic pydantic schema for the JWT token

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    access_token: str
    refresh_token: str
    
    
class TokenPayload(BaseModel):
    """Schema for the token payload

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    """Schema for user authentification

    Args:
        BaseModel (BaseModel): pydantic base model
    """
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24,
                          description="user password")
    

class UserOut(BaseModel):
    """Schema for user's logout

    Args:
        BaseModel (BaseModel): pydantic basic model
    """
    id: UUID
    email: str


class SystemUser(UserOut):
    """Schema for the current user

    Args:
        UserOut (UserOut): inherite from UserOut
    """
    password: str