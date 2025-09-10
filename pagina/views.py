from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from pagina.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, get_user_model, logout
from pagina.forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    return render(request, 'pagina/index.html')

# def destinos(request):
#     return render(request, 'pagina/destinos.html')

# def articulos(request):
#     return render(request, 'pagina/articulos.html') 

def contacto(request):
    return render(request, 'pagina/contacto.html')

class ContacView(View):
    def get (self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

#----------------------------------------------------------------------------------------------
#register
#----------------------------------------------------------------------------------------------

class UserRegisterView(View):
    template_name = 'pagina/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User = get_user_model()
            user = User.objects.create_user(username=username, email=email, password=password)

            login(request, user)

            return redirect('destinos') 
        return render(request, self.template_name, {'form': form})
    

class UserLogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

#---------------------------------------------------------------------
# LoginView Iniciar Sesion
#---------------------------------------------------------------------

class UserLogin(View):
    template_name= 'pagina/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('destinos')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('destinos')
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user= authenticate(request, username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, self.template_name, {
                    'form': form,
                    'error_message': 'Nombre de usuario o contraseña incorrectos'
                })
        return render(request, self.template_name, {'form': form})


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
    
#------------------------------------------------------------------------------------------------
#create
#-------------------------------------------------------------------------------------------------
class CountryCreateView(LoginRequiredMixin, View):
    template_name= 'pagina/create/country_create.html'


    def get (self, request, *args, **kwargs):
        return render (request, self.template_name)

    def post(self, request, *args, **kwargs):
        name= request.POST.get("name")
        description= request.POST.get("description")
        content = request.POST.get("content")
        flag_photo= request.FILES.get("flag_photo")
        iso_code= request.POST.get("iso_code")

        new_country = Country.objects.create(
            name= name,
            description= description,
            content = content, 
            flag_photo = flag_photo,
            iso_code = iso_code
        )

        return redirect('destinos')
    

class CountryListView(LoginRequiredMixin, View):
    template_name = 'pagina/destinos.html'
    paginate_by= 3

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        countries= Country.objects.all()
    
        if query:
            countries = countries.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(iso_code__icontains=query)
            ).distinct()

        paginator = Paginator(countries, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'countries': page_obj.object_list,
            'query': query
        }
        return render(request, self.template_name, context)

#--------------------------------------------------------------------------------------------
#detail
#-------------------------------------------------------------------------------------------
class CountryDetailView(LoginRequiredMixin, View):
    template_name = 'pagina/detail/country.html'

    def get(self, request, id, *args, **kwargs):
        country= get_object_or_404(Country, id=id)
        return render(request, self.template_name, {'country': country})
    
#---------------------------------------------------------------------------------------------
# Update 
#--------------------------------------------------------------------------------------------

class CountryUpdateView(LoginRequiredMixin, View):
    template_name = 'pagina/update/country_update.html'

    def get(self, request, id, *args, **kwargs):
        country = get_object_or_404(Country, id=id)
        return render(request, self.template_name, {'country': country})

    def post(self, request, id, *args, **kwargs):
        country = get_object_or_404(Country, id=id)
        country.name = request.POST.get("name")
        country.description = request.POST.get("description")
        country.content = request.POST.get("content")
        country.flag_photo = request.FILES.get("flag_photo", country.flag_photo)
        country.iso_code = request.POST.get("iso_code")
        country.save()
        return redirect('destinos')

#----------------------------------------------------------------------------------------------
#delete
#---------------------------------------------------------------------------------------------
class CountryDeleteView(View):
    template_name = 'pagina/delete/country_delete.html'

    def get(self, request, id, *args, **kwargs):
        country= get_object_or_404(Country, id=id)
        return render(request, self.template_name, {'country': country})

    def post(self, request, id, *args, **kwargs):
        country = get_object_or_404(Country, id=id)
        country.delete()
        return redirect('destinos')


class ArticleCreateView(View):
    template_name= 'pagina/create/article_create.html'

    def get (self, request, *args, **kwargs):
        return render (request, self.template_name)

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        places = request.POST.get("places")

        new_article = Articulo.objects.create(
            title= title,
            description= description,
            image= image,
            places=places
        )

        return redirect('articulos')

class ArticleListView(View):
    template_name = 'pagina/articulos.html'

    def get(self, request, *args, **kwargs):
        articles = Articulo.objects.all()
        return render(request, self.template_name, {'articles': articles})
    

class ArticleDetailView(View):
    template_name = 'pagina/detail/article.html'

    def get(self, request, id, *args, **kwargs):
        articulo= get_object_or_404(Articulo, id=id)
        return render(request, self.template_name, {'articulo': articulo})

class ArticleUpdateView(View):
    template_name = 'pagina/update/article_update.html'

    def get(self, request, id, *args, **kwargs):
        articulo = get_object_or_404(Articulo, id=id)
        return render(request, self.template_name, {'articulo': articulo})

    def post(self, request, id, *args, **kwargs):
        articulo = get_object_or_404(Articulo, id=id)
        articulo.title = request.POST.get("title")
        articulo.description = request.POST.get("description")
        articulo.image = request.FILES.get("image", articulo.image)
        articulo.places = request.POST.get("places")
        articulo.save()
        return redirect('articulos')
    

class ArticleDeleteView(View):
    template_name = 'pagina/delete/article_delete.html'

    def get(self, request, id, *args, **kwargs):
        articulo= get_object_or_404(Articulo, id=id)
        return render(request, self.template_name, {'articulo': articulo})

    def post(self, request, id, *args, **kwargs):
        articulo = get_object_or_404(Articulo, id=id)
        articulo.delete()
        return redirect('articulos')