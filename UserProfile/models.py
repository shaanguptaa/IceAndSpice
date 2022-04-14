from django.db import models
from Menu.models import Menu
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return self.item.item_name + ' - ' + str(self.quantity)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00) # change default to the total calculated
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)