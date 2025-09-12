VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def check_credentials(username: str, password: str):
    if not username or not password:
        return False, "empty_fields"
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return True, ""
    return False, "invalid_credentials"