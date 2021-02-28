from main import get_following


def test_get_following(mocker):
    mocker.patch("main.get_following", return_value=2)
    assert get_following("SERGIOALOB") == 2
