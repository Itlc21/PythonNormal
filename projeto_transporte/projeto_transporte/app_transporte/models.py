# app_transporte/models.py
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=50)
    cnh = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
