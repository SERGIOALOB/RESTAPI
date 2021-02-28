def test_get(client, insert_first_data):
    res = client.get("/post/1")
    expected = {
        "surname": "Mola",
        "lastname": "Mazo",
        "name": "Charlie",
        "github_name": "SERGIOALOB",
        "github_following": 2,
        "id": 1,
    }
    assert res.status_code == 200
    assert res.json == expected
