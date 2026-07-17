from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from .models import Participante, Cliente

def login_view(request):
    erro = None
    if request.method == 'POST':
        identificador = request.POST.get('identificador', '').strip()
        if identificador:
            if Participante.objects.filter(identificador=identificador).exists():
                erro = "Este nome já está cadastrado no experimento. Por favor, utilize outro nome ou adicione um sobrenome para diferenciar."
            else:
                participante = Participante.objects.create(identificador=identificador)
                request.session['participante_id'] = participante.id
                return redirect('selecao')
    return render(request, 'experimento/cadastro.html', {'erro': erro})

def selecao_view(request):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
    participante = get_object_or_404(Participante, id=participante_id)
    
    # Calcular estatísticas para Interface A
    parts_a = Participante.objects.annotate(
        num_a=Count('clientes', filter=Q(clientes__interface='interface-a'))
    )
    stats_a = {
        'iniciaram': parts_a.filter(num_a__gte=1).count(),
        'concluiram': parts_a.filter(num_a__gte=5).count(),
    }
    
    # Calcular estatísticas para Interface B
    parts_b = Participante.objects.annotate(
        num_b=Count('clientes', filter=Q(clientes__interface='interface-b'))
    )
    stats_b = {
        'iniciaram': parts_b.filter(num_b__gte=1).count(),
        'concluiram': parts_b.filter(num_b__gte=5).count(),
    }
    
    return render(request, 'experimento/selecao.html', {
        'participante': participante,
        'stats_a': stats_a,
        'stats_b': stats_b
    })

def interface_a_view(request):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
    participante = get_object_or_404(Participante, id=participante_id)
    clientes = Cliente.objects.filter(participante=participante).order_by('-criado_em')
    return render(request, 'experimento/interface_a.html', {
        'participante': participante,
        'clientes': clientes,
        'origem': 'interface-a'
    })

def interface_b_view(request):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
    participante = get_object_or_404(Participante, id=participante_id)
    clientes = Cliente.objects.filter(participante=participante).order_by('-criado_em')
    return render(request, 'experimento/interface_b.html', {
        'participante': participante,
        'clientes': clientes,
        'origem': 'interface-b'
    })

@require_POST
def criar_cliente_view(request):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
    
    participante = get_object_or_404(Participante, id=participante_id)
    origem = request.POST.get('origem', 'selecao')
    
    nome = request.POST.get('nome', '')
    email = request.POST.get('email', '')
    cargo_ou_funcao = request.POST.get('cargo_ou_funcao', '')
    codigo_registro = request.POST.get('codigo_registro', '')
    
    Cliente.objects.create(
        participante=participante,
        nome=nome,
        email=email,
        cargo_ou_funcao=cargo_ou_funcao,
        codigo_registro=codigo_registro,
        interface=origem
    )
    
    if origem == 'interface-a':
        return redirect('interface_a')
    elif origem == 'interface-b':
        return redirect('interface_b')
    return redirect('selecao')

@require_POST
def excluir_cliente_view(request, pk):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
        
    participante = get_object_or_404(Participante, id=participante_id)
    cliente = get_object_or_404(Cliente, pk=pk, participante=participante)
    
    origem = request.POST.get('origem', 'selecao')
    cliente.delete()
    
    if origem == 'interface-a':
        return redirect('interface_a')
    elif origem == 'interface-b':
        return redirect('interface_b')
    return redirect('selecao')

def survey_view(request):
    participante_id = request.session.get('participante_id')
    if not participante_id:
        return redirect('login')
    return render(request, 'experimento/survey.html')
