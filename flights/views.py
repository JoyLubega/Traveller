from rest_framework import generics
from .models import Flights
from .serializers import FlightSerializer


class FlightsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer