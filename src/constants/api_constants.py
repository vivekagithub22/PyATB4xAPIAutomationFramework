# APIConstants - class which contains all the endpoints
# Folder that keeps all urls

class APIConstants():
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_get_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_put_patch_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)

