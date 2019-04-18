from django.db import models
from django.utils import timezone




# class User(models.Model):
#       username = models.CharField(max_length=255)
#       email = models.EmailField()
#       password = models.CharField(max_length=255)

#       def __str__(self):
#         return "{},{}".format(self.name,self.email)

class Booking(models.Model):
      pickup = models.CharField(max_length=255)
      destination = models.CharField(max_length=255)
      departure_date = models.CharField(max_length=255)
      return_date = models.CharField(max_length=255)
      no_travellers = models.CharField(max_length=255)
      passport_number=models.CharField(max_length=255)
      date_created = models.DateTimeField( default= timezone.now)
      date_modified = models.DateTimeField(default=timezone.now)
      
      def __str__(self):
        return "{},{}".format(self.destination,self.return_date)