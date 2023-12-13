from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class transaction(models.Model):
    transaction_to = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    transaction_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.IntegerField()
    transaction_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.transaction_on and self.id:
            self.order_id = self.transaction_on.strftime("PAYMENTS%Y%m%dODR") + str(
                self.id
            )
        return super().save(*args, **kwargs)
