from django.urls import path
from . import views

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('getReservationDetails/', views.get_reservation_details),
    # path('get_reservations/', views.get_reservations, name='get_reservations'),
]
