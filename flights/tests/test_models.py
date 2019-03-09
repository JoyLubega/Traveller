from django.test import TestCase

from ..models import Booking


class BookingModelTestCase(TestCase):
    """This class defines the test suite for the flights model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.destination = 'dest'
        self.booked_flight = Booking(destination=self.destination)

    def test_model_can_create_a_booking(self):
        """Test the flight model can create a flight."""
        old_count = Booking.objects.count()
        self.booked_flight.save()
        new_count = Booking.objects.count()
        self.assertNotEqual(old_count, new_count)

