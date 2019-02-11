from rest_framework import serializers
from .models import Flights


class FlightSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Flights
        fields = ('id',
                  'flight_number',
                  'tail_number',
                  'pickup_point',
                  'destination',
                  'flight_time',
                  'airline',
                  'aircraft_type',
                  'flight_date',
                  'date_created',
                  'date_modified')
        
    