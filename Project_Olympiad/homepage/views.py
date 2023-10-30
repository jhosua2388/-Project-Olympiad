from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'homepage/index.html')

def quienes(request):
    
     return render(request, 'homepage/quienes.html')

def servicios(request):
    
     return render(request, 'homepage/servicios.html')

def contacto(request):
    
     return render(request, 'homepage/contacto.html')