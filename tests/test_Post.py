import json
from unittest import mock


def test_post(client):
    input_data = {
        "surname": "Mola",
        "lastname": "Mazo",
        "name": "Charlie",
        "github_name": "SERGIOALOB",
    }

    expected_response = {
        "surname": "Mola",
        "lastname": "Mazo",
        "name": "Charlie",
        "github_name": "SERGIOALOB",
        "github_following": 1,
    }

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
                return self.json_data

    response = MockResponse([{"login": "a"}], 200)
    with mock.patch("main.requests.get", return_value=response):
        res = client.post(
            "/posts",
            json=input_data,
            headers={"Content-Type": "application/json"},
        )

    response_json = res.json

    assert res.status_code == 200
    assert response_json["name"] == expected_response["name"]
    assert response_json["surname"] == expected_response["surname"]
    assert response_json["lastname"] == expected_response["lastname"]
    assert response_json["github_following"] == expected_response["github_following"]
