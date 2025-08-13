from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_persona, name='crear_persona'),
    path('lista/', views.lista_personas, name='lista_personas'),
    path('eliminar/<str:dni>/', views.eliminar, name='eliminar'),
    path('editar/<str:dni>/', views.editar, name='editar'),
]