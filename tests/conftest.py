import pytest

from app.main import server
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def client():
    return TestClient(server)


def pytest_configure():
    pytest.product = None
