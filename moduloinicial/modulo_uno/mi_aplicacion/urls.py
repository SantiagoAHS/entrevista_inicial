# mi_aplicacion/urls.py
from django.urls import path
from . import views
from .views import formulario_view

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', formulario_view, name='formulario'),
]
