from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField(default=0)
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
