import json

import pytest


def test_Post(client):
    data = {
        "surname": "Mola",
        "lastname": "Mazo",
        "name": "Charlie",
        "github_name": "SERGIOALOB",
        "github_following": 2,
    }
    res = client.post(
        "/posts", data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    assert res.json["name"] == data["name"]
    assert res.json["surname"] == data["surname"]
    assert res.json["lastname"] == data["lastname"]
