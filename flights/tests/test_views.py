from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Flights
from ..serializers import FlightSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_flight(
        flight_number="",
         destination="",
         pickup_point="",
         flight_time="",
         airline="",
         aircraft_type="",
         tail_number=""):
        
        Flights.objects.create(flight_number=flight_number, 
                destination=destination,
                pickup_point=pickup_point,
                flight_time=flight_time,
                airline=airline,
                aircraft_type=aircraft_type,
                tail_number=tail_number
                )

    def setUp(self):
        # add test data
        self.create_flight(
         flight_number=1,
         destination="peru",
         pickup_point="ebb",
         flight_time=2,
         airline="KLM",
         aircraft_type="Boeing",
         tail_number="BW23"

        )
        


class GetAllFlightsTest(BaseViewTest):

    def test_get_all_flights(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("flights-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Flights.objects.all()
        serialized = FlightSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)