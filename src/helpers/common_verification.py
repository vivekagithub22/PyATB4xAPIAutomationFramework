# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON schema


def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, " Failed Status Code Match"


def verify_response_key(key, expected_data): #response data verification
    assert key == expected_data, "Failed, response data not match"


def verify_json_key_for_not_null(key): #booking id verification
    assert key != 0, "Failed - Key is Empty" + key
    assert key > 0, "Failed - Key is not greater than zero"
    assert type(key) == int, "Failed - Key is not an integer"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is Empty" + key


def verify_response_delete(response):
    assert "Created" in response
