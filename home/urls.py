# from django.urls import path #tạo ra các đường dẫn path
from django.urls import path
from . import views #gọi file view trong home
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.index),
  path('contact/', views.contact, name="contact"),
  path('register/', views.register, name="register"),
  path('login/', auth_views.login, {'pages/login.html'}, name='login')
]
