from django.shortcuts import render, redirect
from .models import Formulario

def Preencher_Form(request):
    if request.method == 'GET':
        return render(request, 'Screens/formulario.html')
    elif request.method == 'POST':
        data = request.POST.get('date_input')
        atividade = request.POST.get('atividade_input')
        horimetro_final = request.POST.get('horimetro_final_input')
        horimetro_abastecimento = request.POST.get('horimetro_abastecimento_input')
        quantidade_litros = request.POST.get('quant_litros_input')

        # bd | minha variável
        form = Formulario(
            data = data,
            atividade = atividade,
            horimetro_final = horimetro_final,
            horimetro_abastecimento = horimetro_abastecimento,
            quantidade_litros = quantidade_litros
        )

        form.save()
        return redirect('form_preenc')
