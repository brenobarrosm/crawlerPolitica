from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def politico(request):
    politicos = Politico.objects.order_by("name").all()
    return render(request, 'politicos.html', {'politicos': politicos})

def listapoliticos(request):
    search = request.GET.get('search')

    if search:
        politicos = Politico.objects.filter(
            namefantasy__icontains=search.upper())
    else:
        politicos = Politico.objects.order_by("namefantasy").all()

    return render(request, 'listarDeputado.html', {'listaPoliticos': politicos})

def presencaplenario(request):
    politicos = Politico.objects.all()
    presencas = PresencaPlenario.objects.all()
    return render(request, 'presencaplenario.html', {'listaPoliticos': politicos, 'listaPresencas': presencas})

def perfil(request, id):
    politico = Politico.objects.get(id=id)
    presenca = PresencaPlenario.objects.get(politico=id)
    if Gastos.objects.filter(politico=id).exists():
        gasto = Gastos.objects.get(politico=id)
    else:
        gasto = None
    bibliografia = Biograph.objects.get(politico=id)
    votos_nominais = VotosNominais.objects.get(politico=id)
    emendas_aprovadas = EmendasAprovadas.objects.get(politico=id)
    return render(request, 'perfil.html',
                  {'politicos': politico, 'listaPresenca': presenca, 'gastos': gasto, 'bibliografia': bibliografia,
                  'votosNominais': votos_nominais, 'emendasAprovadas': emendas_aprovadas})