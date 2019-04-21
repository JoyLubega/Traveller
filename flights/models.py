from django.db import models
from django.utils import timezone

class Flight(models.Model):
      pickup = models.CharField(max_length=255)
      destination = models.CharField(max_length=255)
      departure_date = models.CharField(max_length=255)
      return_date = models.CharField(max_length=255)
      no_travellers = models.CharField(max_length=255)
      passport_number=models.CharField(max_length=255)
      date_created = models.DateTimeField( default= timezone.now)
      date_modified = models.DateTimeField(default=timezone.now)
      user=models.ForeignKey('auth.User', related_name='flights', on_delete=models.CASCADE)

      def __str__(self):
        return "{},{},{}".format(self.user,self.destination,self.return_date)