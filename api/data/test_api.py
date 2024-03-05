from fastapi.testclient import TestClient
from main import app
from database import get_db, Base
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    # Dependency override

    def override_get_db():
        try:

            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


def test_ping(client):
    res = client.get('/')
    assert res.status_code == 200


def test_signup(client):
    data = {
        "email": "test_user@gmail.com",
        "password": "M2tqjbch+1906"
    }
    
    res = client.post("/api/signup", json=data)
    assert res.status_code == 200
    password = data['password']
    assert len(password) > 5
    assert len(password) < 24