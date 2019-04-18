from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Booking
from ..serializers import BookingSerializer, UserSerializer
from .base import BaseViewTest

        
class BookingTestCase(BaseViewTest):

    def test_get_all_bookedflights(self):
        """
        This test ensures that all flights added in the setUp method
        exist when we make a GET request to the flights/ endpoint
        """
        self.login_client('test_user', 'testing')        # hit the API endpoint
        response = self.client.get(reverse("flights"))
        # fetch the data from db
        expected = Booking.objects.all()
        serialized = BookingSerializer(expected, many=True)
        print(response.data)
        self.assertEqual(response.data['booked_flights'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
