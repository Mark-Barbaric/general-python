import pytest
from fastapi.testclient import TestClient
from src.system_design.rest.fastapi_basic.app.main import app


@pytest.fixture
def test_fast_api_client():
    test_client = TestClient(app)
    return test_client
