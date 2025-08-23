from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'pagina/index.html')

def destinos(request):
    return render(request, 'pagina/destinos.html')

def articulos(request):
    return render(request, 'pagina/articulos.html') 

def contacto(request):
    return render(request, 'pagina/contacto.html')

class Paris(View):
    def get(self, request):
        return render(request, 'pagina/country/paris.html')

class roma(View):
    def get(self, request):
        return render(request, 'pagina/country/roma.html')

class berlin(View):
    def get(self, request):
        return render(request, 'pagina/country/berlin.html')

class londres(View):
    def get(self, request):
        return render(request, 'pagina/country/londres.html')

class tokio(View):
    def get(self, request):
        return render(request, 'pagina/country/tokio.html')

class new_york(View):
    def get(self, request):
        return render(request, 'pagina/country/nuevayork.html')

class rio_de_janeiro(View):
    def get(self, request):
        return render(request, 'pagina/country/rio.html')

class sydney(View):
    def get(self, request):
        return render(request, 'pagina/country/sydney.html')

class barcelona(View):
    def get(self, request):
        return render(request, 'pagina/country/barcelona.html')
    
class amanecer(View):
    def get(self, request):
        return render(request, 'pagina/amanecer.html')
    
class america(View):
    def get(self, request):
        return render(request, 'pagina/america.html')
    
class consejos(View):
    def get(self, request):
        return render(request, 'pagina/consejos.html')
    
class playas(View):
    def get(self, request):
        return render(request, 'pagina/playas.html')
    
class festival(View):
    def get(self, request):
        return render(request, 'pagina/festival.html')
    
class deportes(View):
    def get(self, request):
        return render(request, 'pagina/deportes.html')