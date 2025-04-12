from django.urls import path
from app_form import views

urlpatterns = [
    path("", views.Preencher_Form, name="form_preenc")
]
