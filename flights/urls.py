from django.urls import path
from .views import FlightsView


urlpatterns = [
    path('flights/', FlightsView.as_view(), name="flights-all")
]