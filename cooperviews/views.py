from unicodedata import name
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from django_tables2 import SingleTableView
from cooperviews.models import chk_table, chk_tabl, createAssociado, Associados
from .tables import PersonTable
from .forms import CheckUser, CreateAssociado, CheckCpf

class PersonListView(SingleTableView):
    model = Associados
    tables_class = PersonTable
    template_name = 'accounts/ver_associados_page.html'

def home(request):
    return HttpResponse('Home page')

def principal(request):
    return render(request, 'accounts/principalpage.html')

def cadastrar(request):
    context = {}
    context['form'] = CreateAssociado()
    return render(request, 'accounts/cadastrarpage.html', context)

def gerenciar(request):
    context = {}
    context['form'] = CheckCpf()
    return render(request, 'accounts/gerenciarassociados_page.html', context)

def login(request):
    context = {}
    context['form'] = CheckUser()
    return render(request, 'registration/login.html', context)

def redirect_view(request):
    context = {}
    context['form'] = CheckUser()
    login_data = request.POST.dict()
    user = login_data.get("user")
    senha = login_data.get("password")

    check = chk_table(user, senha)
    if check == True:
        response = render(request, 'accounts/principalpage.html')
    else:
        response = render(request, 'registration/login.html', context)
    return response

def createUser(request):
    context = {}
    context['form'] = CheckUser()
    login_data = request.POST.dict()

    cpf= login_data.get("cpf")
    nomeAssociado= login_data.get("nome")
    quotas= login_data.get("quotas")
    nomeRespoAssociado= login_data.get("nomeresponsavel")
    dt_nasct= login_data.get("datadenascimento")
    cidadeNatal= login_data.get("cidadenatal")
    estadoNatal= login_data.get("estadonatal")
    estadoNatal = estadoNatal.upper()
    telefone= login_data.get("telefone")
    email= login_data.get("email")
    email = email.lower()
    rg= login_data.get("rg")
    isAssociado= login_data.get("associado")
    if isAssociado == "on":
        isAssociado = True
    else:
        isAssociado = False
    cargo= login_data.get("cargo")
    cargo = cargo.title()
    rua= login_data.get("rua")
    rua = rua.title()
    bairro= login_data.get("bairro")
    bairro = bairro.title()
    cidadeAtual= login_data.get("cidade")
    cidadeAtual = cidadeAtual.title()
    cep= login_data.get("cep")
    associado = createAssociado(cpf, nomeAssociado, quotas, nomeRespoAssociado, dt_nasct, cidadeNatal, estadoNatal, telefone, email, rg, isAssociado, cargo, rua, bairro, cidadeAtual, cep)
    print(associado)
    response = render(request, 'accounts/principalpage.html')
    return response

def checkCpf(request): #checa o cpf e já adiciona as informacoes nos campos necessarios da proxima pagina
    login_data = request.POST.dict()
    cpf = login_data.get("cpf")
    data = Associados.objects.get(cpf=cpf)
    initial_data = {
        'cpf' : data.cpf,
        'nome' : data.nomeAssociado,
        'quotas' : data.quotas,
        'nomeresponsavel' : data.nomeRespoAssociado,
        'datadenascimento' : data.dt_nasct,
        'cidadenatal' : data.cidadeNatal,
        'estadonatal' : data.estadoNatal,
        'telefone' : data.telefone,
        'email' : data.email,
        'rg' : data.rg,
        'associado' : data.isAssociado,
        'cargo' : data.cargo,
        'rua' : data.rua,
        'bairro' : data.bairro, 
        'cidade' : data.cidadeAtual,
        'cep' : data.cep
    }
    print()
    
    form = CreateAssociado(initial=initial_data)
    context = {
        'data': data,
        'form': form
    }

    check = chk_tabl(cpf)
    if check == True:
        response = render(request, 'accounts/gerenciarapage.html', context)
    else:
        response = render(request, 'registration/login.html', context)
    return response

def updateAssociado(request):
    login_data = request.POST.dict()
    print("1")
    cpf= login_data.get("cpf")
    nomeAssociado= login_data.get("nome")
    quotas= login_data.get("quotas")
    nomeRespoAssociado= login_data.get("nomeresponsavel")
    dt_nasct= login_data.get("datadenascimento")
    cidadeNatal= login_data.get("cidadenatal")
    estadoNatal= login_data.get("estadonatal")
    estadoNatal = estadoNatal.upper()
    telefone= login_data.get("telefone")
    email= login_data.get("email")
    email = email.lower()
    rg= login_data.get("rg")
    isAssociado= login_data.get("associado")
    if isAssociado == "on":
        isAssociado = True
    else:
        isAssociado = False
    cargo= login_data.get("cargo")
    cargo = cargo.title()
    rua= login_data.get("rua")
    rua = rua.title()
    bairro= login_data.get("bairro")
    bairro = bairro.title()
    cidadeAtual= login_data.get("cidade")
    cidadeAtual = cidadeAtual.title()
    cep= login_data.get("cep")
    associados = Associados(cpf=cpf, nomeAssociado=nomeAssociado, quotas=quotas, nomeRespoAssociado=nomeRespoAssociado, dt_nasct=dt_nasct, cidadeNatal=cidadeNatal, estadoNatal=estadoNatal, telefone=telefone, email=email, rg=rg, isAssociado=isAssociado, cargo=cargo, rua=rua, bairro=bairro, cidadeAtual=cidadeAtual, cep=cep)
    associados.save()
    print("associados")
    response = render(request, 'accounts/principalpage.html')
    return response
# Create your views here.
