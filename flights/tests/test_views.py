from django.urls import reverse
from json import loads, dumps
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Flight
from ..serializers import FlightSerializer, UserSerializer
from .base import BaseViewTest

        
class FlightTestCase(BaseViewTest):

    def test_get_all_bookedflights(self):
        """
        This test ensures that all flights added in the setUp method
        exist when we make a GET request to the flights/ endpoint
        """
        self.login_client('test_user', 'testing')        # hit the API endpoint
        response = self.client.get(reverse("flights"))
        
        expected = Flight.objects.all()
        serialized = FlightSerializer(expected, many=True)
        
        self.assertEqual(response.data['booked_flights'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_a_flight(self):
        """
        This test ensures that a single flight of a given id is returned
        """
        self.login_client('test_user', 'testing')
       
        fli = Flight.objects.get()
        response = self.fetch_a_flight(fli.id)
        
        # fetch the data from db
        expected = Flight.objects.all()
        
        serialized = FlightSerializer(expected, many=True)
        self.assertEqual(response.data, loads(dumps(serialized.data))[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.fetch_a_flight(100)
        self.assertEqual(
            response.data["message"],
            "Flight with id: 100 does not exist"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_flight(self):
        """
        This test ensures that a flight can be added
        """
        self.login_client('test_user', 'testing')
        # hit the API endpoint
        response = self.client.post(
            reverse('flights'),
            self.flight_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_flight_with_missing_fields(self):
        """
        This test ensures that a flight can not  be added with missing fields
        """
        self.login_client('test_user', 'testing')
        response = self.client.post(
            reverse('flights'),
            format="json")
        self.assertEqual(response.data['message'], "All Data is required")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_update_flight(self):
        self.login_client('test_user', 'testing')
        flight = Flight.objects.get()
       
        new_flight = {
            "departure_date":"toay", 
            "destination":"as",
            "pickup":"ebbs",
            "return_date":"tommorrow",
            "no_travellers":2,
            "passport_number":"BCV",
            
        }
        res = self.client.put(
            reverse('flights-detail', kwargs={'id': flight.id}),
            new_flight, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_flight_with_missing_fields(self):
        self.login_client('test_user', 'testing')
        flight = Flight.objects.get()
       
        response = self.client.put(
            reverse('flights-detail', kwargs={'id': flight.id}),
        format="json"
        )
        self.assertEqual(response.data['message'], "All Data is required")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_flight(self):
        self.login_client('test_user', 'testing')
        flight = Flight.objects.get()
        response = self.client.delete(
            reverse('flights-detail', kwargs={'id': flight.id}),
            format="json",
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_flight_does_not_exist(self):
        self.login_client('test_user', 'testing')
        flight = Flight.objects.get()
        response = self.client.delete(
            reverse('flights-detail', kwargs={'id': 100}),
            format="json",
            follow=True)
        self.assertEqual(response.data['message'], "Flight with id: 100 does not exist")
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)