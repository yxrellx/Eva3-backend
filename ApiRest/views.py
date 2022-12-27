from django.shortcuts import render
from Clinica.models import Animal,Emp,Persona
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PersonaSerializer, AnimalSerializer,EmpSerializer
from rest_framework import generics, mixins
# Create your views here.


class Persona_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Persona_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class Emp_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Emp_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



class Animal_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Animal_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset =  Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)