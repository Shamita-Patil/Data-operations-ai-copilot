import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.app.core.database import get_db

from backend.tests.database import (
    TestingSessionLocal,
)


def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[
    get_db
] = override_get_db


@pytest.fixture
def client():

    with TestClient(app) as client:
        yield client