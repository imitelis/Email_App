"""import os, sys
PROJECT_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.pardir)
sys.path.append(PROJECT_ROOT)"""

import pytest
from main import app as flask_app


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["ERROR_404_HELP"] = False
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_hello(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.data == b'{\n    "success": "Hello from the Fake Email server"\n}\n'


def test_invite(client):
    data = {"email": "joedoe@gmail.com"}
    response = client.post("/api/invite", json=data)
    assert response.status_code == 200
    assert (
        response.data
        == b'{\n    "success": "Invitation email was sent to join Fake Email"\n}\n'
    )
