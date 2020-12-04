from django import forms
from django.forms import ModelForm
from .models import Libro, Profile
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import sys
from itertools import cycle

class LibroForm(ModelForm):

    titulo = forms.CharField(min_length=4, max_length=100)
    anio = forms.IntegerField(min_value=1900)
    paginas = forms.IntegerField(min_value=1)

    class Meta:
        model = Libro
        fields=['titulo', 'anio', 'paginas', 'pais', 'autor', 'sinopsis', 'imagen', 'user'] 
        exclude = ('user', 'pais')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['run','fecha_nac', 'telefono', 'region', 'ciudad', 'vivienda']
        widgets={
            'fecha_nac': forms.SelectDateWidget(years=range(1940, 2001)),
            'run': forms.TextInput(attrs={'placeholder': 'Ej: 11222333-k'}),
        }
        labels={
            'fecha_nac':'Fecha de nacimiento'
        }

    def clean_run(self):

        run = self.cleaned_data['run']
        rut = run
        rut = rut.upper();
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            #return true
            return run
        elif dv=="K" and res==10:
            #return true
            return run
        else:
            #return false
            raise forms.ValidationError("El RUN no tiene el formato correcto")

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1','password2']
