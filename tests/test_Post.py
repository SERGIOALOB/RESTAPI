from flask import jsonify
import json


def test_Post(app, client):
    data = {"surname": "Tio", "lastname": "Guay", "name": "Charlie"}
    res = client.post('/posts', data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert res.status_code == 200
