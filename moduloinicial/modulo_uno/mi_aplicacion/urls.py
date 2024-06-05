# mi_aplicacion/urls.py
from django.urls import path
from . import views
from .views import administrar_carreras_grupos, formulario_view
from .views import lista_grupos

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', formulario_view, name='formulario'),
    path('grupos/', views.lista_grupos, name='lista_grupos'),
    path('pantalla_administracion/', views.pantalla_administracion, name='pantalla_administracion'),
    path('get_grupos/<int:carrera_id>/', views.get_grupos, name='get_grupos'),
    path('administrar_carreras_grupos/', administrar_carreras_grupos, name='administrar_carreras_grupos'),
]
