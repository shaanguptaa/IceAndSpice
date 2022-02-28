from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='administrator_index'),
    path('signup', views.handle_admin_signup, name='administrator_signup'),
    path('login', views.handle_admin_login, name='administrator_login'),
    path('logout', views.handle_admin_logout, name='administrator_logout'),
]
