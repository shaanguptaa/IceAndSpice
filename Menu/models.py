from django.db import models
from . import generate_order_id

# Create your models here.
class Menu(models.Model):
    id = models.CharField(max_length=6, default=generate_order_id, primary_key=True, editable=False)
    item_name = models.CharField(max_length=20, default="")
    item_desc = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=10, choices=[("Main", "Main"), ("Drinks", "Drinks"), ("Desserts", "Desserts")], default="Main")
    status = models.CharField(max_length=3, choices=[("IN", "In Stock"), ("OUT", "Out of Stock")], default="IN")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return self.item_name
