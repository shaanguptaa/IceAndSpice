from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from Menu import generate_order_id, generate_menu_id
from IceAndSpice import get_datetime

# Create your models here.
class Menu(models.Model):
    id = models.CharField(max_length=6, default=generate_menu_id, primary_key=True, editable=False)
    item_name = models.CharField(max_length=20, default="")
    item_desc = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=10, choices=[("Main", "Main"), ("Drinks", "Drinks"), ("Desserts", "Desserts")], default="Main")
    status = models.CharField(max_length=3, choices=[("IN", "In Stock"), ("OUT", "Out of Stock")], default="IN")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return self.item_name


# def calc_total(items):
#         total = 0
#         for item in items:
#             total += Menu.objects.get(id=item[0])['price'] * item[1]

#         sum([Menu.objects.filter[id=items]])
#         return total

def calc_t():
        return 100.00

class Order(models.Model):
    id = models.CharField(max_length=6, default=generate_order_id, primary_key=True, editable=False)
    name = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=20, default="")
    items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=calc_t) # change default to the total calculated
    order_date = models.DateTimeField(default=get_datetime)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Order - " + str(self.id)
    
class Cart(models.Model):
    items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00) # change default to the total calculated
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
    

    

    
