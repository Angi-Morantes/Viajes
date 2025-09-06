from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from django.views import View

urlpatterns = [
    path('', views.index, name='index'),
    path('destinos/', views.CountryListView.as_view(), name='destinos'),
    path('articulos/', views.articulos, name='articulos'),
    path('contacto/', views.contacto, name='contacto'),

    #destinos
    path('destinos/paris/', Paris.as_view(), name='paris'),
    path('destinos/roma/', roma.as_view(), name='roma'),
    path('destinos/berlin/', berlin.as_view(), name='berlin'),
    path('destinos/londres/', londres.as_view(), name='londres'),
    path('destinos/tokio/', tokio.as_view(), name='tokio'),
    path('destinos/new-york/', new_york.as_view(), name='nueva york'),
    path('destinos/rio-de-janeiro/', rio_de_janeiro.as_view(), name='rio'),
    path('destinos/sydney/', sydney.as_view(), name='sydney'),
    path('destinos/barcelona/', barcelona.as_view(), name='barcelona'),

    #articulos
    path('articulos/amanecer/', amanecer.as_view(), name= 'amanecer'),
    path('articulos/america/', america.as_view(), name= 'america'),
    path('articulos/consejos/', consejos.as_view(), name= 'consejos'),
    path('articulos/deportes/', deportes.as_view(), name= 'deportes'),
    path('articulos/festivales/', festival.as_view(), name= 'festivales'),
    path('articulos/playas/', playas.as_view(), name= 'playas'),

    #formularios
    path('create_profile/', ContacView.as_view(), name='create_profile' ),
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    #crud
    path('create/country/', CountryCreateView.as_view(), name= 'country_create'),
    path('detail-country/<int:id>', CountryDetailView.as_view(), name='country_detail'),
    path('destinos/<int:id>/update/', CountryUpdateView.as_view(), name='update_country'),
    path('destinos/<int:id>/delete/', CountryDeleteView.as_view(), name='delete_country'),
]
