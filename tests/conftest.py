import pytest
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from src.data.database import Base


MCP_SERVER_URL = "http://localhost:8080"

@pytest.fixture(name="session")
def session_test():

    engine_test: Engine = create_engine(
        "sqlite:///cars_test.db", echo=True, poolclass=StaticPool
    )

    Base.metadata.drop_all(engine_test)
    Base.metadata.create_all(engine_test)

    session = Session(engine_test)

    try:
        yield session
    finally:
        session.close()
