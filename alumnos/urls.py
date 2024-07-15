from django.urls import path
from . import views
from alumnos import views

# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('menu', views.index, name='menu'),
    path('comprar', views.comprar, name='comprar'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<str:codigo>/', views.eliminar_producto, name='eliminar_producto'),
    path('lista/', views.lista_productos, name='lista_productos'),

]


