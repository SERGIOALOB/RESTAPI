import requests
import json


def test_Get():
    url = "http://localhost:5000/post/5"

    payload = {'id': '5', 'name': 'Clau', 'surname': 'Bertol', 'lastname': 'Laguna'}

    headers = {'Content-Type': 'application/json'}

    resp = requests.get(url, headers=headers, data=json.dumps(payload, indent=1))

    resp_body = resp.json()
    assert resp_body['name'] == payload['name']
    print(resp.text)
