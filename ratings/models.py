from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_rating(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(max_length=500)
    submit_by = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
