from django.db import models
from IceAndSpice import get_datetime
from Menu.models import Menu
from django.contrib.auth.models import User

from Order import generate_order_id

# Create your models here.
class OrderItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return self.item.item_name + ' - ' + str(self.quantity)


class Order(models.Model):
    id = models.CharField(max_length=6, default=generate_order_id, primary_key=True, editable=False)
    name = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=20, default="")
    items = models.ManyToManyField(OrderItem)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00) # change default to the total calculated
    order_date = models.DateTimeField(default=get_datetime)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=[("D", "Delivered"), ("N", "Confirmed, Not Yet Delivered"), ('C', 'Cancelled'), ('P', 'Pending')], default="P")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Order - " + str(self.id)
