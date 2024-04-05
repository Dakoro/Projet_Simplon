import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(os.getcwd()).parent.parent
BDD_URI = os.path.join(ROOT_DIR, 'scripts', 'bdd', 'bdd.db')

engine = create_engine(f'sqlite:///{BDD_URI}', echo=True)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(session_factory)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
