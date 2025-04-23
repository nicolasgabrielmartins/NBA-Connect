from balldontlie import BalldontlieAPI
from django.shortcuts import render 

api = BalldontlieAPI(api_key="7e021d5b-0e74-447c-b321-418a88a4a7ca")

def search_players(request):
    nome = request.GET.get("nome", "")
    jogadores_data = []

    if nome:
        response = api.nba.players.list(search=nome)
        jogadores_data = response.data  # Lista de jogadores encontrados

    return render(request, 'players.html', {'jogadores': jogadores_data, 'nome': nome})

def details(request, jogador_id):
    try:
        response = api.nba.players.get(jogador_id)
        jogador = response.data
        return render(request, 'details.html', {'jogador': jogador})
    except Exception as e:
        return render(request, 'details.html', {'erro': str(e)})