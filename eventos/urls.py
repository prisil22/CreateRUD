from django.urls import path
from .import views

urlpatterns = [
     path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/nuevo/', views.gestionar_evento, name='nuevo_evento'),
    path('eventos/editar/<int:id>/', views.gestionar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nuevo/', views.nueva_categoria, name='nueva_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),


]