from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','email', 'password')
		widgets = {
			'username': forms.TextInput(attrs=
				{
				'class': 'form-control', 
				'placeholder': 'Nombre de usuario'
				}),
			'email': forms.TextInput(attrs=
				{
				'class': 'form-control', 
				'placeholder': 'Ingresa email', 
				'type':'email'
				}),
			'password': forms.TextInput(attrs=
				{
				'type': 'password',
				'class': 'form-control',
				'placeholder': 'Ingresa contrasena'
				})
		}
class LoginForm(forms.Form):
	username = forms.CharField(max_length=10, min_length=1, required=True,widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Ingresa un usuario'}))
	password = forms.CharField(max_length=10, min_length=1, required=True, 
		widget = forms.TextInput(attrs={'type': 'password', 
			'class': 'form-control', 'placeholder': 'Ingresa una contrasena'}))
