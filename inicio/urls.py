from django.urls import path
from . import views

urlpatterns = [
    path('crear/clase1/', views.crear_clase1, name='crear_clase1'),
    # Define rutas para crear clases 2 y 3 y otras vistas
    path('buscar/', views.buscar, name='buscar'),
    path('exito/', views.exito, name='exito'),
]
