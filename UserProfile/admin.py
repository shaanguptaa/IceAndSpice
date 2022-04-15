from django.contrib import admin
from UserProfile.models import Profile, Cart, CartItem

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItem)