from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth import login, logout
from homepage import views

# Create your views here.

def homeback(request):
    return render (request, 'homepage.html')

def login(request):
    return render (request, 'user/login.html')

def logout1(request):
    logout(request)
    messages.success(request, f'Te has deslogueado correctamente')
    return render (request, 'user/logout.html')

def create_user(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} fue creado con éxito')
            return redirect('homeback')
    else:
        form = RegistroUsuarioForm() 
    context={'form': form}
    return render (request, 'user/create.html', context)

def indexback(request):
    return render (request, 'user/index.html')