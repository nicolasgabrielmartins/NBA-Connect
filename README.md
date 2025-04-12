# 🏀 NBA Connect

Plataforma para fãs de basquete acompanharem seus jogadores e times favoritos da NBA com estatísticas atualizadas, gráficos de desempenho e notificações personalizadas.

## 🚀 Tecnologias
- Django + Django REST Framework
- PostgreSQL
- Chart.js
- API pública da NBA (balldontlie.io)

## ⚙️ Como rodar localmente

```bash
git clone https://github.com/seu-usuario/nba-connect.git
cd nba-connect
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## 📌 Funcionalidades (v1)
- Autenticação de usuários
- Favoritar jogadores e times
- Estatísticas com gráficos por temporada
- Integração com API externa
- Envio de e-mails com alertas

## 📸 Screenshots
*Em breve...*

## Estrutura de Diretórios (resumo)
nba_connect/
├── nba_connect/             # Configuração principal do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # App para autenticação e perfis
├── players/                 # App para dados dos jogadores
├── teams/                   # App para dados dos times
├── stats/                   # App para estatísticas e gráficos
├── templates/               # HTMLs
├── static/                  # Arquivos estáticos (CSS/JS)
├── media/                   # Uploads de imagens
├── requirements.txt
├── .env.example             # Exemplo de arquivo de variáveis
├── README.md
└── manage.py

# Estrutura Inicial do Projeto NBA Connect

# Requisitos (requirements.txt)
django>=4.2
djangorestframework
django-environ
psycopg2-binary
requests

# .gitignore
__pycache__/
*.pyc
venv/
.env
db.sqlite3
/static/
/media/

