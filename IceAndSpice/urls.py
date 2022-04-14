"""IceAndSpice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('master-admin/', admin.site.urls),
    path('admin/', include('administrator.urls'), name='administrator'),
    path('', views.index, name='homepage'),
    path('authentication/', include('Authentication.urls'), name='Authentication'),
    path('reservation/', include('Reservation.urls'), name='Reservation'),
    path('user/', include('UserProfile.urls'), name='User'),
    path('order/', include('Order.urls'), name='Order'),
    path('menu/', include('Menu.urls'), name='Menu'),
    path('temp/', views.temp),
    # path('menu/', include('Menu.urls'), name='menu'),
]
