# payloads

def payload_create_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "John",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-02-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": "Dinner"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload