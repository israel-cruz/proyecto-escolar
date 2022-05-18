from django.urls import path

from .views import (
    home, registrar_material, modificar_material,
    lista_material, gestion_material, entrada_material, baja_material,
    login_page, logout_user,
)

urlpatterns = [
    path('', home, name='home'),
    path('lista/', lista_material, name='lista-material'),
    path('gestion/', gestion_material, name='gestion-material'),
    path('registrar-material/', registrar_material, name='registrar-material'),
    path('modificar-material/<str:pk>/', modificar_material, name='modificar-material'),
    path('entrada-material/', entrada_material, name='entrada-material'),
    path('baja-material/<str:pk>/', baja_material, name='baja-material'),

    path('logout/', logout_user, name='logout'),
    path('login/', login_page, name='login'),
]