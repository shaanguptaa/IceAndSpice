from django.urls import path
from . import views

urlpatterns = [
    path('user-profile', views.index, name='user-profile'),
    path('signup', views.handle_signup, name='signup'),
    path('login', views.handle_login, name='login'),
    # path('login/<redirect_loc>', views.handle_login, name='login_redirect'),
    path('logout', views.handle_logout, name='logout'),
    path('get-orders', views.get_orders),
]
 