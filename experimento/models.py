from django.db import models

class Participante(models.Model):
    identificador = models.CharField(max_length=255, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identificador

class Cliente(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='clientes')
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cargo_ou_funcao = models.CharField(max_length=255)
    codigo_registro = models.CharField(max_length=255)
    interface = models.CharField(max_length=20, default='interface-a')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.codigo_registro}"
