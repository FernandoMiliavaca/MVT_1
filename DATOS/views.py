from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.
def familia(request):
    familiar1 = Familia(nombre = 'Mario', edad = 33, fecha_de_nacimiento = 1989-4-22)

    familia.save()
    datos = f'Nombre ---> {familia.nombre} \n Edad ---> {familia.edad} \n Fecha de nacimiento ---> {familia.fecha_de_nacimiento}'
    return HttpResponse (datos)