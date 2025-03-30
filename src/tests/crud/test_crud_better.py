#Conftest

import pytest
import allure

from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *


class TestCRUDBooking(object):

    @pytest.mark.positive
    @allure.title("TC3 - Verify Get booking")
    @allure.description("Verify get booking response and the status code 200")
    def test_get_booking_TC(self, create_booking_id):
        get_booking_response = get_request(url=APIConstants().url_get_booking(booking_id=create_booking_id),
                                           auth=None)
        print(get_booking_response)

    @pytest.mark.positive
    @allure.title("TC4 - Verify update booking")
    @allure.description("Verify update booking response and the status code 200")
    def test_put_update_booking(self, create_token, create_booking_id):
        booking_id = create_booking_id
        token = create_token

        put_url = APIConstants().url_put_patch_delete(booking_id=create_booking_id)
        put_update_booking_response = put_requests(url=put_url,
                                                   auth=None,
                                                   headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
                                                   payload=payload_update_booking(),
                                                   in_json=False)
        print(put_update_booking_response.json())
        verify_http_status_code(response_data=put_update_booking_response, expected_data=200) #Status code verification
        verify_response_key(key=put_update_booking_response.json()["firstname"], expected_data="Jim") #Response data verification
        verify_response_key(key=put_update_booking_response.json()["lastname"], expected_data="John")

    @pytest.mark.positive
    @allure.title("TC5 - Verify Delete booking")
    @allure.description("Verify delete booking and the status code 201")
    def test_delete_booking(self, create_token, create_booking_id):
        token = create_token
        booking_id = create_booking_id
        delete_booking_response = delete_requests(url=APIConstants().url_put_patch_delete(booking_id=booking_id),
                                                  auth=None,
                                                  headers=Utils().common_header_put_delete_patch_cookie(token=token),
                                                  in_json=False)
        verify_http_status_code(response_data=delete_booking_response, expected_data=201)





