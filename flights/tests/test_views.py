from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Booking, User
from ..serializers import BookingSerializer, UserSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_booking(
         departure_date="",
         destination="",
         pickup="",
         return_date="",
         no_travellers="",
         passport_number=""):
        
        Booking.objects.create(departure_date=departure_date, 
                destination=destination,
                pickup=pickup,
                return_date=return_date,
                no_travellers=no_travellers,
                passport_number=passport_number
                )

    def setUp(self):
        # add test data
        self.create_booking(
        departure_date="today", 
        destination="kla",
        pickup="ebbs",
        return_date="tommorrow",
        no_travellers=2,
        passport_number="3"
        )
        
class GetAllBookingTest(BaseViewTest):

    def test_get_all_bookedflights(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the flights/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("flights")
        )
        # fetch the data from db
        expected = Booking.objects.all()
        serialized = BookingSerializer(expected, many=True)
        print(response.data)
        print(serialized.data)
        self.assertEqual(response.data['booked_flights'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)