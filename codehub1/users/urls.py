
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name='users'#namespacing

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',LoginView.as_view(template_name="users/login.html"),name='login'),
    path('profile/',views.profile,name='profile'),
]