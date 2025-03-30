from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *

import pytest
import allure


@pytest.fixture#(scope="session")
def create_token():
    create_token_response = post_request(url=APIConstants().url_create_token(),
                                         auth=None,
                                         headers=Utils().common_headers_json(),
                                         payload=payload_create_token(),
                                         in_json=False)
    verify_http_status_code(response_data=create_token_response, expected_data=200)
    verify_json_key_for_not_null_token(key=create_token_response.json()["token"])
    token=create_token_response.json()["token"]
    print(token)
    return token

@pytest.fixture#(scope="session")
def create_booking_id():
    create_booking_id_response = post_request(url=APIConstants().url_create_booking(),
                                              auth=None,
                                              headers=Utils().common_headers_json(),
                                              payload=payload_create_booking(),
                                              in_json=False)

    verify_http_status_code(response_data=create_booking_id_response, expected_data=200)
    booking_id = create_booking_id_response.json()["bookingid"]
    verify_json_key_for_not_null(key=booking_id)
    print(booking_id)
    return booking_id