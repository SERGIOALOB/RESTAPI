from main import get_following, app, APIException
from unittest import mock
from unittest.mock import patch
import unittest
import pytest
from werkzeug import exceptions
import flask
import unittest


def test_get_following(mock_github_response):
    response = mock_github_response([{"login": "a"}, {"login": "b"}], 200)
    with mock.patch("main.requests.get", return_value=response):
        assert get_following("SERGIOALOB") == 2

    response = mock_github_response([{"login": "a"}], 200)
    with mock.patch("main.requests.get", return_value=response):
        assert get_following("SERGIOALOB") == 1

    response = mock_github_response({"error": "User not found"}, 400)
    with mock.patch("main.requests.get", return_value=response):
        with pytest.raises(APIException):
            get_following("adbhifpasd")