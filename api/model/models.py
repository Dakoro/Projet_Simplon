from sqlalchemy import Column, String
from database import Base


class User(Base):
    __tablename__ = "UserApiModel"

    id = Column(String(255), primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(24), nullable=False)
