from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.index, name='user-profile'),
    path('addToCart/', views.add_to_cart, name='addToCart'),
    path('removeFromCart/', views.remove_from_cart, name='removeFromCart'),
    path('getCart/', views.get_cart, name="getCart"),
    path('getCartItems/', views.get_cart_items, name='getCartItems'),
    # path('get-orders', views.get_orders),
]
