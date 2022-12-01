from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Template, Context 

# Create your views here.
def familia(request):
    familiar1 = Familia(nombre = 'Mario', edad = 33, fecha_de_nacimiento = '1989-4-22')
    familiar2 = Familia(nombre = 'Jose' , edad = 30, fecha_de_nacimiento = '1992-04-03')
    familiar3 = Familia(nombre = 'Carmen', edad = 55, fecha_de_nacimiento = '1967-5-22')

    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    diccionario={'persona1':familiar1, 'persona2':familiar2, 'persona3':familiar3}

    archivo=open('/Users/fernandomiliavaca/Documents/Programacion/Python/MVT_FERNANDOMILIAVACA/MVT_FERNANDOMILIAVACA/MVT_FERNANDOMILIAVACA/templates/MVT_FERNANDOMILIAVACA/familia.html')
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    documento = template.render(contexto)

    return HttpResponse(documento)