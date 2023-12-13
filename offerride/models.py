from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class travel_ride(models.Model):
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    seats = models.IntegerField()
    travel_date = models.DateField()
    travel_time = models.TimeField()
    price = models.IntegerField()
    distance = models.IntegerField(null=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
