from django.contrib import admin
from UserProfile.models import Cart, CartItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)