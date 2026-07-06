from django.contrib import admin
from .models import Participante, Cliente

class ClienteInline(admin.TabularInline):
    model = Cliente
    extra = 0
    fields = ('nome', 'email', 'cargo_ou_funcao', 'codigo_registro', 'criado_em')
    readonly_fields = ('criado_em',)

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'criado_em')
    inlines = [ClienteInline]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'participante', 'email', 'cargo_ou_funcao', 'codigo_registro', 'criado_em')
    list_filter = ('participante',)
