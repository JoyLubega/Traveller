from rest_framework import serializers
from .models import Booking, User


class BookingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Booking
        fields = ('id',
                  'pickup',
                  'destination',
                  'departure_date',
                  'return_date',
                  'no_travellers',
                  'passport_number',
                  )

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'password',
                  )
        
    