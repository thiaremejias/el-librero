from django.urls import path, include
from . import views
from .views import LibroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('peliculas', LibroViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('padrino/', views.padrino, name="padrino"),
    path('factotum/', views.factotum, name="factotum"),
    path('torero/', views.torero, name="torero"),
    path('borges/', views.borges, name="borges"),
    path('listado-peliculas/', views.listado_peliculas, name="listado-peliculas"),
    path('agregar-pelicula/', views.agregar_pelicula, name="agregar-pelicula"),
    path('modificar-pelicula/<id>/', views.modificar_pelicula, name="modificar-pelicula"),
    path('eliminar-pelicula/<id>/', views.eliminar_pelicula, name="eliminar-pelicula"),
    path('eliminar-pelicula-recomendaciones/<id>/', views.eliminar_pelicula_recomendaciones, name="eliminar-pelicula-recomendaciones"),
    path('recomendaciones/', views.visualizar_recomendaciones, name="recomendaciones"),
    path('registro-usuario/', views.registrar_usuario, name="registro-usuario"),
    path('perfil/', views.perfil, name="perfil"),
    path('api/', include(router.urls)), #url de la api -> localhost:8000/api/peliculas
]