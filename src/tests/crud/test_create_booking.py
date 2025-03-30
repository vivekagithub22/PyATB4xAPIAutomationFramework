#URL -> constants -> api_constants.py
#headers -> Utils -> utils.py
#payload -> helpers -> payload_manager.py
#request -> helpers -> api_request_wrapper.py
#status code verification -> helpers -> common_verification.py
#response verification -> helpers -> common_verification.py

""" Imports """
import pytest
import allure

from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *
import logging

""" Test cases """

@pytest.mark.positive
@allure.title("TC1- verify that create booking status 200 & booking ID shouldn't be null")
@allure.description("Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
def test_create_booking_positive_TC1():
    #LOGGER = logging.getLogger(__name__)
    #LOGGER.info("Starting the Testcase - TC1 - positive")
    create_booking_response = post_request(url=APIConstants().url_create_booking(),
                                           auth=None,
                                           headers=Utils().common_headers_json(),
                                           payload=payload_create_booking(),
                                           in_json=False)
    verify_http_status_code(response_data=create_booking_response, expected_data=200) #Status code verification
    verify_json_key_for_not_null(key=create_booking_response.json()["bookingid"]) #booking id verification
    verify_response_key(key=create_booking_response.json()["booking"]["firstname"],expected_data="Amit") #Response data verification
    #LOGGER.info(create_booking_response.json()["bookingid"])
    #LOGGER.info("End of the Testcase TC1 -positive")
    #Logger is used instead of print command

@pytest.mark.negative
@allure.title("TC2 - verify that create booking doesn't work with no payload")
@allure.description("Create a booking with empty payload and verify bookingid is not created")
def test_create_booking_negative_TC2():
    create_booking_response = post_request(url=APIConstants().url_create_booking(),
                                           auth=None,
                                           headers=Utils().common_headers_json(),
                                           payload={},
                                           in_json=False)
    verify_http_status_code(response_data=create_booking_response, expected_data=500) #Status code verification





# Run -> pytest src/tests/crud/test_create_booking.py --alluredir=allure_result
# Run -> allure serve allure_result