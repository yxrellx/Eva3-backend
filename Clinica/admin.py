from django.contrib import admin
from Clinica.models import Persona
from Clinica.models import Emp
from Clinica.models import Animal

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'celular', 'direccion', 'nacionalidad', 'sexo']
# Register your models here.
admin.site.register(Persona,PersonaAdmin)



class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'sexo', 'raza', 'edad', 'f_nacimiento','dueño','veterinario']
# Register your models here.
admin.site.register(Animal,AnimalAdmin)



class EmpAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'cargo', 'direccion', 'nacionalidad', 'sexo']
# Register your models here.
admin.site.register(Emp,EmpAdmin)

list_filter = ('Emp',)