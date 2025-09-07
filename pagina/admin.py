from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User, Country, Articulo

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'content', 'iso_code', 'flag_photo')
    search_fields = ('name', 'description')
    list_editable = ( 'description', 'content', 'iso_code', 'flag_photo')
    list_filter = ('name', 'description')
    list_per_page = 3
    # exclude = ('description')

@admin.register(Articulo)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'places')
    search_fields = ('title', 'description')
    list_editable = ( 'description', 'image', 'places')
    list_filter = ('title', 'description')
    list_per_page = 2
    # exclude = ('description')
