from main import get_following
from unittest import mock


def test_get_following(mocker):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    response = MockResponse([{"login": "a"}, {"login": "b"}], 200)
    with mock.patch("main.requests.get", return_value=response):
        assert get_following("SERGIOALOB") == 2

    response = MockResponse([{"login": "a"}], 200)
    with mock.patch("main.requests.get", return_value=response):
        assert get_following("SERGIOALOB") == 1
