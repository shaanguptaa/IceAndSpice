from django.urls import path
from Menu import views

urlpatterns = [
    # path('', views.menu, name='menu_index'),
    path('order/', views.order, name='order'),
]
