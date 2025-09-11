from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User, Country, Articulo, Profile, Review

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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'country', 'photo')
    search_fields = ('user', 'first_name', 'last_name', 'phone', 'country')
    list_editable = ('first_name', 'last_name')
    list_filter = ('user', 'country')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'text', 'date')
    search_fields = ('user', 'article', 'text')
    list_editable = ('text',)  
    list_filter = ('text',) 