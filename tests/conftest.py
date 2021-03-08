import pytest
import json
from unittest import mock
from main import app as flask_app
from main import requests
from requests.exceptions import HTTPError

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def insert_first_data(client):
    data = {
        "surname": "Mola",
        "lastname": "Mazo",
        "name": "Charlie",
        "github_name": "SERGIOALOB",
        "github_following": 2,
    }
    client.post(
        "/posts", data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    return "DATA INSERTED"


@pytest.fixture
def mock_github_response():
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        def json(self):
            return self.json_data
        def raise_for_status(self):
            if self.status_code != 200:
                raise HTTPError(response=self)

    return MockResponse