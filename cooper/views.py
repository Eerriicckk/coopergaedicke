from django.shortcuts import render, redirect
'''
'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/'db_coopergaedicke.sqlite',
    }
    databaseadmin
    //D@tabas3AdmiN
    cooper

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from cooper.models import chk_table
from .forms import NameForm

def home(request):
    return HttpResponse('Home page')

def principal(request):
    return render(request, 'accounts/principalpage.html')

def cadastrar(request):
    return render(request, 'accounts/cadastrarpage.html')

def gerenciar(request):
    return render(request, 'accounts/gerenciarassociados_page.html')

def login(request):
    return render(request, 'registration/login.html')

def redirect_view(request):
    user = request.POST['usuario']
    senha = request.POST['senha']
    chk_table(user, senha)
    
    #response = redirect('/redirect-success/')
    #return response

def login_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

'''