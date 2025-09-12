import pytest
from login_logic import check_credentials

@pytest.mark.parametrize("username,password,expected", [
    ("admin", "1234", (True, "")),
    ("wrong", "1234", (False, "invalid_credentials")),
    ("admin", "wrong", (False, "invalid_credentials")),
    ("", "1234", (False, "empty_fields")),
    ("admin", "", (False, "empty_fields")),
    ("", "", (False, "empty_fields")),
    ("a"*500, "b"*500, (False, "invalid_credentials")),
])
def test_check_credentials(username, password, expected):
    assert check_credentials(username, password) == expected