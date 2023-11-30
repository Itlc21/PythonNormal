# app_transporte/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Adicionado para mensagens
from .models import Funcionario
from .forms import FuncionarioForm

def pagina_inicial(request):
    return render(request, 'app_transporte/index.html')

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'app_transporte/lista.html', {'funcionarios': funcionarios})

def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm()
    
    return render(request, 'app_transporte/cadastro.html', {'form': form})

def atualizar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    return render(request, 'app_transporte/atualiza.html', {'form': form, 'funcionario': funcionario})

def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    messages.success(request, 'Funcionário deletado com sucesso!')
    return redirect('lista_funcionarios')
