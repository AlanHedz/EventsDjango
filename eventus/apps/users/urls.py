from django.conf.urls import include, url
from . import views

app_name = 'users_app'

urlpatterns = [
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^salir/$', views.LogOut, name='logout'),
]