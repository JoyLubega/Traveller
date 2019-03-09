from django.contrib import admin
from .models import User, Booking

admin.site.register(Booking)
admin.site.register(User)