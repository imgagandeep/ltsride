from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class notification_message(models.Model):
    news_stuff = models.CharField(max_length=50, null=True)
    messages = models.CharField(max_length=50, null=True)
    publishing_rides = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
