import json


def test_Get(app, client):
    res = client.get('/post/1')
    assert res.status_code == 200
    expected = {"surname": "Bertol", "lastname": "Laguna", "name": "Clau", 'id': 1}
    assert expected == json.loads(res.get_data(as_text=True))
