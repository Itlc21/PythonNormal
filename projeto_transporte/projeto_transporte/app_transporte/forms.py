# app_transporte/forms.py
from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'senha', 'cpf', 'cargo', 'cnh', 'telefone', 'email']
