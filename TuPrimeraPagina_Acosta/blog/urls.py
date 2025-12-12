from django.urls import path
from blog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('crear-autor/', views.crear_autor, name="CrearAutor"),
    path('crear-categoria/', views.crear_categoria, name="CrearCategoria"),
    path('crear-post/', views.crear_post, name="CrearPost"),
    path('buscar-autor/', views.buscar_autor, name="BuscarAutor"),
]