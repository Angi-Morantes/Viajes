from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number= models.CharField(max_length=15, blank=True, null=True)
    address= models.CharField(max_length=255, blank=True, null=True)
    city= models.CharField(max_length=100, blank=True, null=True)
    country= models.CharField(max_length=100, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    uptated_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "users"
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.email})"
    
    # REQUIRED_FIELDS= ["phone_number"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def _str_(self):
        return f"{self.user.username}'s Profile"

class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    flag_photo = models.ImageField(upload_to='flags', blank=True, null=True)
    iso_code = models.CharField(max_length=500)

    class Meta:
        db_table = "countries"
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def _str_(self):
        return self.name

class Articulo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    places = models.JSONField(default=list)

    class Meta:
        db_table = "articles"
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def _str_(self):
        return self.title

class ArticleCountry(models.Model):
    article = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "article_countries"
        verbose_name = 'País del artículo'
        verbose_name_plural = 'Países de los artículos'

    def _str_(self):
        return f"{self.article.title} - {self.country.name}"

class Review(models.Model):
    article = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "reviews"
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return f"{self.user.username}'s Reseña sobre {self.article.title}"
