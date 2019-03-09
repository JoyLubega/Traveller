from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookingSerializer, UserSerializer
from .models import Booking, User


class FlightsView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request):
       booked_flights = Booking.objects.all()
       serializer = BookingSerializer(booked_flights, many=True)
       return Response({"booked_flights": serializer.data})

    def post(self, request):
        booking ={
            'pickup':request.data.get('pickup'),
            'destination': request.data.get('destination'),
            'departure_date':request.data.get('departure_date'),
            'return_date':request.data.get('return_date'),
            'no_travellers':request.data.get('no_travellers'),
            'passport_number': request.data.get('passport_number')
        }

        # Create a booking from the above data
        serializer = BookingSerializer(data=booking)
        if serializer.is_valid(raise_exception=True):
            booking_saved = serializer.save()
        return Response({"success": "Booking with id: '{}' created successfully".format(booking_saved.id)})


class UsersView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request):
       users = User.objects.all()
       serializer = UserSerializer(users, many=True)
       return Response({"users": serializer.data})

    def post(self, request):
        user ={
            'name':request.data.get('name'),
            'email': request.data.get('email'),
            'password':request.data.get('password'), 
        }
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            saved_user = serializer.save()
        return Response({"success": "User - '{}' has been created successfully".format(saved_user.name)})
