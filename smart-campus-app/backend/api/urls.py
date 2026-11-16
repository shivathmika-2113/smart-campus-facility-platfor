from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, FacilityViewSet, BookingViewSet, TicketViewSet
router = DefaultRouter()
router.register("facilities", FacilityViewSet)
router.register("bookings", BookingViewSet)
router.register("tickets", TicketViewSet)
urlpatterns = [path("health/", health), path("", include(router.urls))]
