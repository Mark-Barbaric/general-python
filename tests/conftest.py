import pytest
from fastapi.testclient import TestClient
from src.system_design.rest.fastapi_basic.app.main import app
from src.system_design.rest.flask.flask_routers.app import create_app


@pytest.fixture
def test_fast_api_client():
    test_client = TestClient(app)
    return test_client


@pytest.fixture
def test_flask_client():
    app = create_app()
    return app.test_client()
