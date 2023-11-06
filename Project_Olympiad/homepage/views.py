from django.shortcuts import render, HttpResponse, redirect
from backoffice.forms import RegistroBeneficiarios
from django.contrib import messages
from backoffice.models import beneficiarios
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
#creacion de funcion para app contacto

def contacto(request):
    contact_form= ContactForm()
    if request.method == "POST":
          contact_form = ContactForm(data=request.POST)
          if contact_form.is_valid():
             name = request.POST.get('name', '')
             email = request.POST.get('email', '')
             content = request.POST.get('content', '')
             
             
             email = EmailMessage(
                "ONG Hermanos sin Fronteras: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["teamgreenolimpiadas@gmail.com"],
                reply_to=[email]
            )
             try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('Contacto')+"?ok")
             except:
                #Algo no ha ido bien, redireccionamos a FAIL
               return redirect(reverse('Contacto')+"?fail")
             
     
    return render(request, "homepage/contacto.html", {'form':contact_form})

def home(request):
    return render(request,'homepage/index.html')

def quienes(request):
    
     return render(request, 'homepage/quienes.html')

def servicios(request):
    
     return render(request, 'homepage/servicios.html')

def regristros(request):
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
          beneficiario.created_by=0
          beneficiario.fuente="portal"

          #Guardar el registro del beneficiario 
          beneficiario.save()
          messages.success(request, f'El registro de {beneficiario.nombre} fue creado con éxito')
          return redirect('registro')
     else:
        form=RegistroBeneficiarios
     context={'form': form}
     return render(request, 'homepage/registro.html', context)

