from django.urls import path
from .controller import *

app_name = 'auth'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('login-petugas/', login_petugas, name='login_petugas'),
    path('register/', register_pasien, name='register')
]
