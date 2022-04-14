from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    # path('reserve_table/', views.reserve_table, name='reserve_table'),
    # path('get_reservations/', views.get_reservations, name='get_reservations'),
]
