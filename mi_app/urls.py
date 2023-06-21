from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create_player/',views.crear_jugador, name='crear_jugador'),
    path('create_director/',views.crear_director, name='crear_director'),
    path('create_equipo/',views.crear_equipo, name='crear_equipo'),
    path('create_liga/',views.crear_liga, name='crear_liga'),
    path('create_estadio/',views.crear_estadio, name='crear_estadio'),
    path('create_arbitro/',views.crear_arbitro, name='crear_arbitro'),
    path('create_juego/',views.crear_juego, name='crear_juego'),
    path('jugadores/', views.lista_jugadores, name='lista_jugadores'),
    path('directores/', views.lista_directores, name='lista_directores'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('ligas/', views.lista_liga, name='lista_liga'),
    path('estadios/', views.lista_estadios, name='lista_estadios'),
    path('arbitros/', views.lista_arbitros, name='lista_arbitros'),
    path('juegos/', views.lista_juegos, name='lista_juegos'),
    path('equipos/<int:id>', views.equipo_detail, name='equipo_detail'),
    path('ligas/<int:id>', views.liga_detail, name='liga_detail'),
    
]
