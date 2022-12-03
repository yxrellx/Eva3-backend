from django import forms
from Clinica.models import Animal,Persona,Emp
from django.forms.widgets import NumberInput

class FormAnimal(forms.ModelForm): #campos para template wingte
    class Meta:
        model = Animal
        fields = '__all__'
    nombre = forms.CharField(min_length=3,max_length=20)
    especie = forms.CharField(max_length=20)
    sexo = forms.CharField(max_length=10)
    raza = forms.CharField(max_length=15)
    edad = forms.CharField(min_length=2, max_length=50)
    f_nacimiento = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


class FormPersona(forms.ModelForm): #campos para template wingte
    class Meta:
        model = Persona
        fields = '__all__'
    nombre = forms.CharField(min_length=3,max_length=20)
    email = forms.EmailField()
    celular = forms.CharField(max_length=9)
    direccion = forms.CharField(max_length=20)
    nacionalidad = forms.CharField(max_length=20)
    sexo = forms.CharField(max_length=20) 

class FormEmp(forms.ModelForm): #campos para template wingte
    class Meta:
        model = Emp
        fields = '__all__'
    nombre = forms.CharField(min_length=3,max_length=20)
    edad = forms.CharField(min_length=2, max_length=50)
    cargo = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=20)
    nacionalidad = forms.CharField(max_length=20)
    sexo = forms.CharField(max_length=20)

