# projeto_transporte/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Suas outras configurações de URL aqui
    path('admin/', admin.site.urls),
    path('', include('app_transporte.urls')),
    # Adicione mais paths conforme necessário para suas visualizações
]

# Adicione as configurações para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
