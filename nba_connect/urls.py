from django.contrib import admin
from django.urls import path, include
from home.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('players.urls')),
    path('', include('home.urls')),
] #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
