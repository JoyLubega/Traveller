from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .decorators import validate_flight_data
from .models import Flight
from .serializers import FlightSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class FlightView(generics.ListCreateAPIView):
    """
    GET flights/
    POST flights/
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_flight_data
    def post(self, request, *args, **kwargs):
        flight = Flight.objects.create(
            pickup=request.data["pickup"],
            destination=request.data["destination"],
            departure_date= request.data['departure_date'],
            return_date= request.data['return_date'],
            no_travellers = request.data['no_travellers'],
            passport_number=request.data['passport_number'],
            user_id = request.user.id
            

        )
        return Response(
            data=FlightSerializer(flight).data,
            status=status.HTTP_201_CREATED
        )
# get all flights
    def get(self, request):
       booked_flights = Flight.objects.all()
       serializer = FlightSerializer(booked_flights, many=True)
       return Response({"booked_flights": serializer.data})


class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET flight/:id/
    PUT flights/:id/
    DELETE flights/:id/
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get(self, request, *args, **kwargs):
        try:
            flight = self.queryset.get(pk=kwargs["id"])
            return Response(FlightSerializer(flight).data)  
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Flight with id: {} does not exist".format(kwargs["id"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_flight_data
    def put(self, request, *args, **kwargs):
        try:
            flight = self.queryset.get(pk=kwargs["id"])
            serializer = FlightSerializer()
            updated_flight = serializer.update(flight, request.data)
            return Response(FlightSerializer(updated_flight).data)
        except Flight.DoesNotExist:
            return Response(
                data={
                    "message": "Flight with id: {} does not exist".format(kwargs["id"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_flight = self.queryset.get(pk=kwargs["id"])
            a_flight.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Flight.DoesNotExist:
            return Response(
                data={
                    "message": "Flight with id: {} does not exist".format(kwargs["id"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
