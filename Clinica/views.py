from django.shortcuts import render,redirect
from Clinica.models import Animal,Persona,Emp
from Clinica.forms import FormAnimal,FormPersona,FormEmp
# Create your views here.

def index(request):
    return render(request,'Clinica/index.html') 

def listadoAnimal(request):
    animales = Animal.objects.all()
    #animales = Animal.objects.all().filter(nombre="martina", especie="gato")--nombre en especifico y especie
    #animales = Animal.objects.all().filter(nombre="Miguel")---por nombre
    #animales = Animal.objects.all().order_by('-nombre')
    #animales = Animal.objects.all().order_by('nombre')--por abecedario
    data = {'animales': animales}
    return render(request, 'Clinica/animales.html', data)

def agregarAnimal(request):
    form = FormAnimal()
    if request.method == 'POST' :
        form = FormAnimal(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/agregarAnimal.html', data)

def eliminarAnimal(request, id):
    animales = Animal.objects.get(id = id)
    animales.delete()
    return redirect('/animales')

def actualizarAnimal(request, id):
    animales = Animal.objects.get(id = id)
    form = FormAnimal(instance=animales)
    if request.method =='POST' :
        form = FormAnimal(request.POST, instance=animales)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/actualizarAnimal.html', data)

#Dueño

def listadoDueño(request):
    personas = Persona.objects.all()
    #personas = Persona.objects.all().filter(nombre="daniel", direccion="luis flores")
    #personas = Persona.objects.all().filter(nombre="javiera")
    #personas = Persona.objects.all().order_by('-nombre')
    #personas = Persona.objects.all().order_by('nombre')
    data = {'personas': personas}
    return render(request, 'Clinica/personas.html', data)

def agregarDueño(request):
    form = FormPersona()
    if request.method == 'POST' :
        form = FormPersona(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/agregarDueño.html', data)

def eliminarDueño(request, id):
    personas = Persona.objects.get(id = id)
    personas.delete()
    return redirect('/personas')

def actualizarDueño(request, id):
    personas = Persona.objects.get(id = id)
    form = FormPersona(instance=personas)
    if request.method =='POST' :
        form = FormPersona(request.POST, instance=personas)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/actualizarDueño.html', data)

#Doctor

def listadoEmp(request):
    empleado = Emp.objects.all()
    #empleado = Emp.objects.all().filter(nombre="camila", edad="23")
    #empleado = Emp.objects.all().filter(nombre="jaime")
    #empleado = Emp.objects.all().order_by('-nombre')
    #empleado = Emp.objects.all().order_by('id')
    data = {'empleado': empleado}
    return render(request, 'Clinica/empleado.html', data)

def agregarEmp(request):
    form = FormEmp()
    if request.method == 'POST' :
        form = FormEmp(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/agregarEmp.html', data)

def eliminarEmp(request, id):
    empleado= Emp.objects.get(id = id)
    empleado.delete()
    return redirect('/empleado')

def actualizarEmp(request, id):
    empleado = Emp.objects.get(id = id)
    form = FormEmp(instance=empleado)
    if request.method =='POST' :
        form = FormEmp(request.POST, instance=empleado)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Clinica/actualizarEmp.html', data)