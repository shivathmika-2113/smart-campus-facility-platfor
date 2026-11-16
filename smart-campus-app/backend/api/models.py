from django.db import models
class Facility(models.Model):
    name = models.CharField(max_length=120)
    building = models.CharField(max_length=120)
    capacity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, default="Available")
    def __str__(self): return self.name

class Booking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT)
    requester = models.CharField(max_length=120)
    purpose = models.CharField(max_length=240)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=30, default="Pending")
    request_key = models.CharField(max_length=120, blank=True, unique=True, null=True)

class Ticket(models.Model):
    title = models.CharField(max_length=180)
    facility = models.CharField(max_length=120)
    priority = models.CharField(max_length=10, default="M3")
    status = models.CharField(max_length=30, default="New")
    assignee = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    version = models.PositiveIntegerField(default=1)
