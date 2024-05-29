# mi_aplicacion/urls.py
from django.urls import path
from . import views
from .views import formulario_view
from .views import lista_grupos

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', formulario_view, name='formulario'),
    path('grupos/', views.lista_grupos, name='lista_grupos'),
]
