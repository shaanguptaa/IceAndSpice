from django.urls import path
from Menu import views

urlpatterns = [
    # path('', views.menu, name='menu_index'),
    path('getItem/', views.get_item),
    path('addItem/', views.add_item),
    path('updateItem/', views.update_item),
    path('deleteItem/', views.delete_item),
]
