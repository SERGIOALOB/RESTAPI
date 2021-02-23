import json


def test_Post(app, client):
    data = {"surname": "Tio", "lastname": "Guay", "name": "Charlie"}
    res = client.post('/posts', data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert res.status_code == 200
    assert res.json['name'] == data['name']
    assert res.json['surname'] == data['surname']
    assert res.json['lastname'] == data['lastname']