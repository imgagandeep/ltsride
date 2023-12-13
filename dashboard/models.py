from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class travel_prefrence(models.Model):
    chattiness = models.CharField(max_length=50, null=True)
    music = models.CharField(max_length=50, null=True)
    smoking = models.CharField(max_length=50, null=True)
    pets = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class add_car(models.Model):
    country = models.CharField(max_length=50, null=True)
    licence_plate_number = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    car_image = models.ImageField(upload_to="cars/", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
