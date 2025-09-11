from django import forms 
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile, User, Review

class LoginForm(forms.Form):
    username= forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder':'Tu contraseña'})
    )

User = get_user_model()

class RegisterForm(forms.Form):
    username= forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder':"Define tu nombre de usuario"})
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'tu@email.com'})
)
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña'})
)
    password_confirm = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'})
)

    def clean_username(self):
    # Validación para asegurar que el nombre de usuario no exista
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
    # Validación para asegurar que el correo electrónico no exista
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrad.")
        return email

    def clean(self):
    # Validación para asegurar que las contraseñas coincidan
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'country', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña aquí...'}),
        }
