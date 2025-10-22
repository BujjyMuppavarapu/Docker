from app.main import app
from fastapi.testclient import TestClient
import pytest

@pytest.fixture()
def test_app():
    client = TestClient(app)
    yield client
