from django.db import transaction
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Facility, Booking, Ticket
from .serializers import FacilitySerializer, BookingSerializer, TicketSerializer

@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "service": "smart-campus-api"})

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by("-id")
    serializer_class = TicketSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("-id")
    serializer_class = BookingSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        s = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        d = s.validated_data
        overlap = Booking.objects.select_for_update().filter(
            facility=d["facility"], start_at__lt=d["end_at"],
            end_at__gt=d["start_at"], status__in=["Pending", "Approved", "Confirmed"])
        if overlap.exists():
            return Response({"detail": "This facility already has an overlapping booking."},
                            status=status.HTTP_409_CONFLICT)
        self.perform_create(s)
        return Response(s.data, status=status.HTTP_201_CREATED)
