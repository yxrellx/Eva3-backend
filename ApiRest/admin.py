from django.contrib import admin
from Clinica.models import Persona,Emp,Animal
# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'celular', 'direccion', 'nacionalidad', 'sexo']


class EmpAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'cargo', 'direccion', 'nacionalidad', 'sexo']



class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'sexo', 'raza', 'edad', 'f_nacimiento','dueño','veterinario']
