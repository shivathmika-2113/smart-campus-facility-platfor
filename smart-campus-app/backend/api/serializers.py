from rest_framework import serializers
from .models import Facility, Booking, Ticket
class FacilitySerializer(serializers.ModelSerializer):
    class Meta: model = Facility; fields = "__all__"
class BookingSerializer(serializers.ModelSerializer):
    class Meta: model = Booking; fields = "__all__"
class TicketSerializer(serializers.ModelSerializer):
    class Meta: model = Ticket; fields = "__all__"
