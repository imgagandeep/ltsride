from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class register(models.Model):
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    aadhar_number = models.CharField(max_length=30)
    user_image = models.ImageField(upload_to="users/", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class verify_otp(models.Model):
    email_otp = models.IntegerField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
