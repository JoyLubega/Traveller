from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
import json


from ..models import Booking

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_booking(departure_date="", destination="", pickup="", return_date="", no_travellers="", passport_number=""):
        
        Booking.objects.create(departure_date=departure_date, 
                destination=destination,
                pickup=pickup,
                return_date=return_date,
                no_travellers=no_travellers,
                passport_number=passport_number
                )
    
    def login_a_user(self, username="", password=""):
        url = reverse("auth-login" )
        return self.client.post(url, data=json.dumps({"username": username,"password": password}),
            content_type="application/json"
        )
    
    def login_client(self, username="", password=""):
        # get a token from DRF
        response = self.client.post(
            reverse("obtain-token"),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        print(response.data)
        self.token = response.data['token']
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token
    def register_a_user(self, username="", password="", email=""):
        return self.client.post(
            reverse(
                "auth-register",
                kwargs={
                    "version": "v1"
                }
            ),
            data=json.dumps(
                {
                    "username": username,
                    "password": password,
                    "email": email
                }
            ),
            content_type='application/json'
        )

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        # add test data
        self.create_booking(departure_date="today", destination="kla",pickup="ebbs",return_date="tommorrow",no_travellers=2,passport_number="3"
        )
