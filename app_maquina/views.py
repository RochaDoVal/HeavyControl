from django.shortcuts import render, redirect
from .models import Maquinas
# segundo

def Cadastrar_Maquina(request):
    if request.method == 'GET':
        return render(request, 'Screens/cadastro_maquina.html')
    elif request.method == 'POST':
        nome = request.POST.get('input_nome')
        num_serie = request.POST.get('input_numero_serie')
        modelo = request.POST.get('input_modelo')
        fabricante = request.POST.get('input_fabricante')
        horimetro_atual = request.POST.get('input_horimetro_atual')
        categoria = request.POST.get('input_Categoria')
        tipo = request.POST.get('input_tipo')
        ultima_manutencao_horimetro = request.POST.get('input_ultima_manutencao_horimetro')
        data_ultima_manutencao = request.POST.get('input_data')

        maquinas = Maquinas(
            # nome da coluna do bd = oq eu quero add na coluna
            nome = nome,
            numero_serie = num_serie,
            modelo = modelo,
            fabricante = fabricante,
            horimetro_atual = horimetro_atual,
            categoria = categoria,
            tipo = tipo,
            ultima_manutencao_horimetro = ultima_manutencao_horimetro,
            data_ultima_manutencao = data_ultima_manutencao,
        )

        maquinas.save()

        return redirect('cadastrar_maquina')

