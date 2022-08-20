from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
from django.template import loader


# Create your views here.


def familiar (request):

    familiar1= Familiar(nombre = "Marta", apellido = "Gomez", cumpleanios = "2022-06-12", edad = 71, parentesco = "Abuela", ocupacion = "Jubilada") #los objetos son instancias de clase
    familiar1.save()

    familiar2= Familiar(nombre = "Pedro", apellido = "Sanchez", cumpleanios = "2022-04-08",  edad = 18, parentesco = "Hermano", ocupacion = "Estudiante") 
    familiar2.save()

    familiar3= Familiar(nombre = "María", apellido = "Sanchez", cumpleanios = "2022-05-05", edad = 23, parentesco = "Hermana", ocupacion = "Maestra") 
    familiar3.save()

    familiar4= Familiar(nombre = "Roberto", apellido = "Sanchez", cumpleanios = "2022-09-28", edad = 54, parentesco = "Tío", ocupacion = "Taxista") 
    familiar4.save()


    contexto = {

    "familiares": [familiar1, familiar2, familiar3, familiar4] #el diccionario lleva una key y un value. El value del key "familiares" en este caso es una lista de objetos  
    
    }
    

    plantilla = loader.get_template("Template1.html")
    documento = plantilla.render(contexto)

    return HttpResponse(documento)
