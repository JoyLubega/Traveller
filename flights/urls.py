from django.urls import path
from .views import FlightsView, UsersView


urlpatterns = [
    path('flights/', FlightsView.as_view(), name="flights"),
    path('users/', UsersView.as_view(), name="users"),
]