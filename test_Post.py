import requests
import json


def test_Post():
    url = "http://localhost:5000/posts"

    payload = {'name': 'Sergio', 'surname': 'Bertol', 'lastname': 'Laguna'}

    headers = {'Content-Type': 'application/json'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=1))

    resp_body = resp.json()
    assert resp_body['name'] == payload['name']
    assert resp_body['surname'] == payload['surname']
    assert resp_body['lastname'] == payload['lastname']
    print(resp.text)
