import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

BDD_URI = os.getenv('BDD_URI')

engine = create_engine(f'sqlite:///{BDD_URI}', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Generate an sqlalchemy Session instance

    Yields:
        Session: SQLalchemy Session instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
