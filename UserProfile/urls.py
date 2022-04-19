from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.index, name='user-profile'),
    path('addToCart/', views.add_to_cart, name='addToCart'),
    path('removeFromCart/', views.remove_from_cart, name='removeFromCart'),
    path('getCart/', views.get_cart, name="getCart"),
    path('save-changes/', views.update_profile),
    path('checkout/', views.checkout),
    path('repeat-order/', views.checkout),
    path('changeItemQuantity/', views.change_item_quantity),
    path('test/', views.test),
    # path('getCartItems/', views.get_cart_items, name='getCartItems'),
]
