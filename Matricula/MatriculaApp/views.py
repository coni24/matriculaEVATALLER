from django.shortcuts import render
from MatriculaApp.models import Matricula

def index(request):
    return render(request,'templateApp/index.html')

def listaMatricula(request):
    entradas = Matricula.objects.all()
    data = {'entradas': entradas}
    return render(request,'templateApp/entradas.html',data)


#Login
#Crear Matricula
#Actualizar matricula
#Eliminar matricula
#Listar matricula

