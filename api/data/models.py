from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class Author(Base):
    __tablename__ = 'Author'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    article_count = Column(Integer)


class Paper(Base):
    __tablename__ = 'Paper'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    title = Column(String(200))
    source = Column(String(5))
    abstract = Column(Text)  # Using String for TEXT type


class Author_Paper(Base):
    __tablename__ = 'Author_Paper'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('Author.id'))
    paper_id = Column(Integer, ForeignKey('Paper.id'))


class User(Base):
    __tablename__ = "User"

    id = Column(String(255), primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(60), nullable=False)
