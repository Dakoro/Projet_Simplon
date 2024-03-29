from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class Author(Base):
    """Model for the Author table 

    Args:
        Base (Any): declarative base model from SQLalchemy
    """
    __tablename__ = 'Author'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    article_count = Column(Integer)


class Paper(Base):
    """Basic Model class for the Paper table

    Args:
        Base (Any): declarative base model from SQLalchemy
    """
    __tablename__ = 'Paper'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    title = Column(String(200))
    categories = Column(String(30))
    abstract = Column(Text)  # Using String for TEXT type


class Author_Paper(Base):
    """Model for the Author_Paper table

    Args:
        Base (Any): declarative base  model from Sqlalchemy
    """
    __tablename__ = 'Author_Paper'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('Author.id'))
    paper_id = Column(Integer, ForeignKey('Paper.id'))


class User(Base):
    """Model for the UserApiData table

    Args:
        Base (Any): declarative base model from SQLalchemy
    """
    __tablename__ = "UserApiData"

    id = Column(String(255), primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(60), nullable=False)
