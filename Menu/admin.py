from django.contrib import admin
from Menu.models import Menu, Order, Cart, CartItem

# Register your models here.
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
