from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard', views.index, name='administrator_index'),
    # path('signup', views.handle_admin_signup, name='administrator_signup'),
    path('login', views.handle_admin_login, name='administrator_login'),
    path('logout', views.handle_admin_logout, name='administrator_logout'),
    path('save-changes/', views.update_profile),
    path('get-counts/', views.get_counts),
    path('getOffer/', views.get_offer),
    path('updateOffer/', views.update_offer),
    path('deleteOffer/', views.delete_offer),

]
