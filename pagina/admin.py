from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User, Country, Articulo

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Country)
admin.site.register(Articulo)