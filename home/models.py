from django.db import models


# Create your models here.
class contact(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    query = models.TextField(max_length=1000)
    timestamp = models.DateTimeField()
