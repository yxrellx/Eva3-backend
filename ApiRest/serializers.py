from Clinica.models import Persona,Emp,Animal
from rest_framework import serializers


class PersonaSerializer(serializers.ModelSerializer): #campos para template wingte
    class Meta:
        model = Persona
        fields = '__all__' 

class EmpSerializer(serializers.ModelSerializer): #campos para template wingte
    class Meta:
        model = Emp
        fields = '__all__'
  
  
class AnimalSerializer(serializers.ModelSerializer):#campos para template wingte
    class Meta:
        model = Animal
        fields = '__all__'


