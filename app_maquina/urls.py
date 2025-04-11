from django.urls import path
from app_maquina import views

urlpatterns = [
    path("", views.Cadastrar_Maquina, name="cadastrar_maquina")
]