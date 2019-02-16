from rest_framework import viewsets
from .models import Flights
from .serializers import FlightSerializer


class FlightsViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer