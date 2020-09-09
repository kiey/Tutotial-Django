from django.shortcuts import render
from os import listdir
# Create your views here.
def recipes(request, plato):
    return render(request, 'recetas/' + plato + '/index.html')
def home(request):
    return render(request, 'home.html', {'recetas':listdir('receta/templates/recetas')})
