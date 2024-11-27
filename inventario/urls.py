from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('categorias/', views.categorias, name="categoria"),
    path('productos/', views.productoFormView, name="producto"),
    path('', views.index),
]
