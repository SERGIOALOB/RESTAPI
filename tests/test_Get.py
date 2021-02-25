import json


def test_Get(client):
    res = client.get('/post/1')
    assert res.status_code == 200
    expected = {"surname": "Mola", "lastname": "Mazo", "name": "Charlie", "github_name": "SERGIOALOB",
                "github_following": 2, "id": 1}
    assert expected == json.loads(res.get_data(as_text=True))
