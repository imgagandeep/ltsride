from django.db import models
from django.contrib.auth.models import User
from offerride.models import travel_ride

# Create your models here.


class save_ride(models.Model):
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    seats = models.IntegerField()
    travel_date = models.DateField()
    travel_time = models.TimeField()
    price = models.IntegerField()
    timestamp = models.DateTimeField()
    travel_mate = models.CharField(max_length=100)
    ride = models.ForeignKey(travel_ride, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
