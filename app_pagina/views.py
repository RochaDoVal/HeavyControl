from django.shortcuts import render
from app_pagina import views

def incio(request):
    return render(request, 'Screens/index.html')

