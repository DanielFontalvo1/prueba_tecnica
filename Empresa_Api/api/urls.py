from unittest.mock import patch
from django.urls import URLPattern, path
from .views import EmpresaView

urlpatterns = [
    path('empresas/',EmpresaView.as_view(),  name='empresas_list'),
    path('empresas/<int:id>',EmpresaView.as_view(),  name='empresas_process')
]