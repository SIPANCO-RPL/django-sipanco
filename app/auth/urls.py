from django.urls import path
from .controller import *

app_name = 'auth'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login')
]
