from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ['username','first_name','last_name','email','password1','password2']

class RegistroBeneficiarios(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=15, min_length=3, required=True)
    apellido=forms.CharField(label="Apellidos", max_length=15, min_length=3, required=True)
    fecha_nacimiento=forms.DateTimeField(label="Fecha de nacimiento", required=True,widget=forms.DateInput(attrs={'type': 'date'}))
    nacionalidad=forms.CharField(label="Nacionalidad", max_length=15, min_length=3, required=True)
    email=forms.EmailField()
    telefono=forms.CharField(label="Teléfono", max_length=15, required=True)
    pais_residencia=forms.CharField(label="Pais de residencia", max_length=15, required=True)
    grado_educacion=forms.CharField(label="Grado de educación", max_length=15)
    actividad_laboral=forms.CharField(label="Actividad Laboral", max_length=15,required=False)
    profesion=forms.CharField(label="Profesión", max_length=15,required=False)
    
    
"""class otro(): 
    estado="creado"
    created_at=forms.DateTimeField(auto_now_add=True)
    update_at=forms.DateTimeField(auto_now_add=True)
    created_by=forms.IntegerField()
    fuente=forms.CharField(max_length=15)"""
