from django.db import models
from django.utils import timezone

# Create your models here.


class Flights(models.Model):
    flight_number = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=False)
    pickup_point = models.CharField(max_length=255, null=False)
    flight_time = models.CharField(max_length=255, null=False)
    airline= models.CharField(max_length=255, null=False)
    aircraft_type = models.CharField(max_length=255, null=False)
    tail_number = models.CharField(max_length=255, null=False)
    flight_date = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField( default= timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return "{},{},{},{}".format(self.flight_number,self.destination,self.pickup_point,self.airline)

class User(models.Model):
      name = models.CharField(max_length=255)
      email = models.EmailField()
      password = models.CharField(max_length=255)

      def __str__(self):
        return "{},{}".format(self.name,self.email)