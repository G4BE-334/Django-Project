from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.db import connection
from .models import Cliente, Grupo, Recomendacao
import math

grupoN = 0
recomendadorN = 0
grupoJE = 0
clienteN = 0

# Create your views here.
def paginaInicial(request):
    if request.method == 'POST':
        grupal = Grupo()
        nome = request.POST.get('nome')
        telefone = request.POST.get('celular')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data')
        sexo = request.POST.get('sexo')
        grupo = request.POST.get('code')
        grupo = grupo.upper()
        endereco = request.POST.get('endereco')
        cep = request.POST.get('cep')

        grupal, created= Grupo.objects.get_or_create(grupo=grupo)   
        cliente, created = Cliente.objects.get_or_create(nome = nome, cpf=cpf, endereco=endereco, telefone=telefone, datanasc=data_nascimento, sexo=sexo, email=email, cep=cep, grupoid=grupal) #,recomendacaoid=recomendacao)
        
        if (grupal.qtd == 0):
            grupal.criadorid = cliente
        
        grupal.save()
        with connection.cursor() as cursor:
            cursor.execute("UPDATE grupo SET Qtd = Qtd + 1 WHERE Grupo = %s", [grupo])
                
        cliente.save()
        
        global grupoN
        grupoN = cliente.grupoid
        
        return redirect('/paginaGrupo')
    
    return render(request, "index.html")

def paginaGrupo(request):
    global grupoN
    grupal, created = Grupo.objects.get_or_create(grupo = grupoN)
    qtdG = grupal.qtd
    codG = grupal.grupo
    goals = [0, 50, 100, 500, 1000, 5000, 10000, 50000]
    n = 0

    while (qtdG > goals[n]):
        n += 1
    percentageBar = math.ceil((qtdG-goals[n-1])/(goals[n] - goals[n-1]) * 100)
    
    return render(request, "paginaGrupo.html", {"qtdG":qtdG, "codG": codG, "meta": goals[n], "percentageBar": percentageBar})

def login(request):
    if request.method == 'POST':
        cpf2 = request.POST.get('cpf2')
        clienteJE = get_object_or_404(Cliente, cpf = cpf2)
        global grupoN
        grupoN = clienteJE.grupoid
        return redirect('/paginaGrupo')

    return render(request, "login.html")
