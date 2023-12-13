from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class story(models.Model):
    story = models.TextField(max_length=500, null=True)
    timestamp = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class govt_id(models.Model):
    passport = models.ImageField(upload_to="govt/", null=True)
    aadhar_card = models.ImageField(upload_to="govt/", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
