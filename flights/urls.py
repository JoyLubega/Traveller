from django.urls import path
from .flight_views import FlightView, FlightDetailView
from .auth_views import LoginView, RegisterView


urlpatterns = [
    path('flights/', FlightView.as_view(), name="flights"),
    path('flights/<int:id>', FlightDetailView.as_view(), name="flights-detail"),
    path('login/', LoginView.as_view(), name="auth-login"),
    path('register/', RegisterView.as_view(), name="auth-register"),
    
]