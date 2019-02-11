from django.test import TestCase

from ..models import Flights


class ModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.flight_number = 1
        self.flight = Flights(flight_number=self.flight_number)

    def test_model_can_create_a_flight(self):
        """Test the flight model can create a flight."""
        old_count = Flights.objects.count()
        self.flight.save()
        new_count = Flights.objects.count()
        self.assertNotEqual(old_count, new_count)

