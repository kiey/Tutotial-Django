from django.shortcuts import render
import random
# Create your views here.
def home_page_view(request):
   return render(request, 'hola_mundo.html')

def about_page_view(request):
   numero_fav = random.randint(0,100)
   parametros = {'numero_favorito': numero_fav}
   return render(request, 'about.html', parametros)
