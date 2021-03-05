from main import get_following, app, MyException
from unittest import mock
from unittest.mock import patch
import unittest
import pytest
from werkzeug import exceptions
import flask
import unittest


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

    with mock.patch("main.requests.get", side_effect=exceptions.BadRequest):
        try:
            get_following("adbhifpasd")
            assert False
        except MyException as exc:
            assert True
