from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=10)
    sexo = models.CharField(max_length=50)

    def nombre_persona(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.nombre_persona()

    class Meta:
        verbose_name = 'Persona'   
        verbose_name_plural = 'Personas'
        db_table = 'Persona'
        ordering = ['nombre']


class Emp(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10) 

    def nombre_emp(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.nombre_emp()

    class Meta:
        verbose_name = 'Emp'   
        verbose_name_plural = 'Emps'
        db_table = 'Emp'
        ordering = ['nombre']

class Animal(models.Model):
    dueño = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Emp, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    f_nacimiento = models.DateField()

    



