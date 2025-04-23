from django.urls import path
from . import views

urlpatterns = [
    path('buscar-jogadores/', views.search_players, name='search_players'),
    path('jogador/<int:jogador_id>/', views.details, name='details'),
]
