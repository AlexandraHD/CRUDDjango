from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add/', views.add_reg),
    path('delete/<id>', views.delete_reg),
    path('edit/<id>', views.edit_reg),
    path('update/<id>', views.update_reg)
]