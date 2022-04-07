from django.urls import path
from Menu import views

urlpatterns = [
    # path('', views.menu, name='menu_index'),
    path('order/', views.order, name='order'),
    path('addToCart/', views.add_to_cart, name='addToCart'),
    path('removeFromCart/', views.remove_from_cart, name='removeFromCart'),
    path('getCart/', views.get_cart, name="getCart"),
    path('getCartItems/', views.get_cart_items, name='getCartItems'),
]
