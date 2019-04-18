# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from ..models import Booking, User
# from ..serializers import BookingSerializer, UserSerializer
# from .base import BaseViewTest

        
# class BookingTestCase(BaseViewTest):

#     def test_get_all_bookedflights(self):
#         """
#         This test ensures that all songs added in the setUp method
#         exist when we make a GET request to the flights/ endpoint
#         """
#         # hit the API endpoint
#         response = self.client.get(reverse("flights"))
#         # fetch the data from db
#         expected = Booking.objects.all()
#         serialized = BookingSerializer(expected, many=True)
#         self.assertEqual(response.data['booked_flights'], serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class UserTestCase(BaseViewTest):
    
#     def test_get_all_bookedflights(self):
#         """
#         This test ensures that all songs added in the setUp method
#         exist when we make a GET request to the flights/ endpoint
#         """
#         response = self.client.get(reverse("flights"))
#         expected = Booking.objects.all()
#         serialized = BookingSerializer(expected, many=True)
#         self.assertEqual(response.data['booked_flights'], serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)