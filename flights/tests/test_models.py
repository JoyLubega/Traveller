from .base import BaseViewTest
from ..models import Flight
from django.contrib.auth.models import User


class FlightModelTestCase(BaseViewTest):
    """This class defines the test suite for the flights model."""       
    def test_model_can_create_a_flight(self):
        """Test the flight model can create a flight."""
        old_count = 0
        new_count = Flight.objects.count()
        self.assertNotEqual(old_count, new_count)

