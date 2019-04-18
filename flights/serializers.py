from rest_framework import serializers
from .models import Booking
from django.contrib.auth.models import User


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
        model = User
        fields = ("username", "email")
        
class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)