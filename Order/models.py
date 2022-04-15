from django.db import models
from IceAndSpice import get_datetime
from Menu.models import Menu
from django.contrib.auth.models import User

from Order import generate_order_id

# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=6, default=generate_order_id, primary_key=True, editable=False)
    name = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=20, default="")
    items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00) # change default to the total calculated
    order_date = models.DateTimeField(default=get_datetime)
    delivered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Order - " + str(self.id)