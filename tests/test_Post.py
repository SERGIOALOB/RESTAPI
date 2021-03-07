import json
from unittest import mock


def test_post_success(client, mock_github_response):
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

    response = mock_github_response([{"login": "a"}], 200)
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



def test_post_error(client, mock_github_response):
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

    response = mock_github_response([{"error": "not found"}], 400)
    with mock.patch("main.requests.get", return_value=response):
        res = client.post(
            "/posts",
            json=input_data,
            headers={"Content-Type": "application/json"},
        )

    response_json = res.json
    assert res.status_code == 400
    assert response_json == {'message': 'Github user not found'}