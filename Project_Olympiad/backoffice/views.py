from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm 
from django.contrib.auth import login, logout
from homepage import views
from .models import beneficiarios


from .forms import RegistroBeneficiarios

# Create your views here.

def homeback(request):
    return render (request, 'homepage.html')

def login(request):
    return render (request, 'user/login.html')

def logout_backoffice(request):
    logout(request)
    messages.success(request, f'Te has deslogueado correctamente')
    return redirect('inicio')

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

def create_beneficiario(request):
    if request.method=='POST':
        form=RegistroBeneficiarios(request.POST)
        if form.is_valid():
            beneficiario=beneficiarios()
            beneficiario.nombre=form.cleaned_data['nombre']
            beneficiario.apellido=form.cleaned_data['apellido']
            beneficiario.fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            beneficiario.nacionalidad=form.cleaned_data['nacionalidad']
            beneficiario.email=form.cleaned_data['email']
            beneficiario.telefono=form.cleaned_data['telefono']
            beneficiario.pais_residencia=form.cleaned_data['pais_residencia']
            beneficiario.grado_educacion=form.cleaned_data['grado_educacion']
            beneficiario.actividad_laboral=form.cleaned_data['actividad_laboral']
            beneficiario.profesion=form.cleaned_data['profesion']
            beneficiario.estado="creado"
            beneficiario.created_by=1
            beneficiario.fuente="backoffice"

            #Guardar el registro del beneficiario 
            beneficiario.save()
            messages.success(request, f'El registro de {beneficiario.nombre} fue creado con éxito')
            return redirect('registro2')
    else:
        form=RegistroBeneficiarios()
    context={'form': form}
    return render(request, 'beneficiario/registro2.html', context)