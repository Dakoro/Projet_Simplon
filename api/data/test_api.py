import pytest
import sqlalchemy as sa
from fastapi.testclient import TestClient
from httpx import Client, WSGITransport
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
from models import User, Paper, Author

from database import Base
from main import app, get_db
from utils import get_hashed_password

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = sa.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up the database once
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


# These two event listeners are only needed for sqlite for proper
# SAVEPOINT / nested transaction support. Other databases like postgres
# don't need them. 
# From: https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#serializable-isolation-savepoints-transactional-ddl
@sa.event.listens_for(engine, "connect")
def do_connect(dbapi_connection, connection_record):
    """handle engine connection and behaviors

    Args:
        dbapi_connection (Any): connection
        connection_record (Any): connection history
    """
    # disable pysqlite's emitting of the BEGIN statement entirely.
    # also stops it from emitting COMMIT before any DDL.
    dbapi_connection.isolation_level = None


@sa.event.listens_for(engine, "begin")
def do_begin(conn):
    """handle the engine begin

    Args:
        conn (Any): connection object
    """
    # emit our own BEGIN
    conn.exec_driver_sql("BEGIN")


@pytest.fixture()
def session():
    """pytest fixture to handle the Sqlalchemy Session

    Yields:
        Session: Sqlalchemy Session instance
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Begin a nested transaction (using SAVEPOINT).
    nested = connection.begin_nested()

    # If the application code calls session.commit, it will end the nested
    # transaction. Need to start a new one when that happens.
    @sa.event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.begin_nested()

    yield session

    # Rollback the overall transaction, restoring the state before the test ran.
    session.close()
    transaction.rollback()
    connection.close()


# A fixture for the fastapi test client which depends on the
# previous session fixture. Instead of creating a new session in the
# dependency override as before, it uses the one provided by the
# session fixture.
@pytest.fixture()
def client(session):
    """Client Instance to perform resquest to the api

    Args:
        session (Session): Session instance to handle database query
    """
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]


def test_ping(client):
    """Ping the api

    Args:
        client (TestClient): TestClient Instance
    """
    res = client.get('/')
    assert res.status_code == 200


@pytest.fixture()
def token(client, session):
    """Fixture to handle identification with JWT token

    Args:
        client (_type_): _description_
        session (_type_): _description_

    Returns:
        _type_: _description_
    """
    data_sign = {
        "email": "test_user@gmail.com",
        "password": "M2tqjbch+1906"
    }
    
    res = client.post("/api/signup", json=data_sign)
    assert res.status_code == 200
    password = data_sign['password']
    assert len(password) > 5
    assert len(password) < 24

    query = sa.select(User)
    user = session.execute(query).all()[0][0]
    assert user.email == data_sign['email']
    
    data_login = {
        "username": "test_user@gmail.com",
        "password": "M2tqjbch+1906"
    }
    
    res_login = client.post("/api/login", data=data_login)
    res_login_data = res_login.json()
    token = res_login_data['access_token']
    assert res_login.status_code == 200
    assert list(res_login_data.keys()) == ['access_token', 'refresh_token']
    assert token is not None
    return token
    


def test_protected_route(client, session, token):
    """Test the accest to the protected route with correct login auth
       with JWT token

    Args:
        client (TestClient): Client to send request
        session (Session): Handle request to database
        token (str): JWT token
    """
    author_route = "/api/author/"
    paper_route = "/api/paper/"
    authors_route = "/api/authors/"
    papers_route = "/api/papers/"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    new_author = Author(id=1, name="Author1", article_count=1)
    new_paper = Paper(id=1, year=2024, categories='science', title="Paper1", abstract="abstract")
    
    session.add(new_author)
    session.add(new_paper)
    session.commit()
    
    res_author = client.get(author_route, params={"author_id": 1}, headers=headers)
    res_paper = client.get(paper_route, params={"paper_id": 1}, headers=headers)
    res_authors = client.get(authors_route, params={"offset": 10, "limit": 10}, headers=headers)
    res_papers = client.get(papers_route, params={"offset": 10, "limit": 10}, headers=headers)
    
    assert res_authors.status_code == 200
    assert res_papers.status_code == 200
    assert res_author.status_code == 200
    assert res_paper.status_code == 200
        
    
    
    
    
    