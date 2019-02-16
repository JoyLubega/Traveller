from django.urls import path
from .views import FlightsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('flights', FlightsViewSet, base_name='flights')
urlpatterns = router.urls