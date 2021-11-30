from django.urls import path
from . import views


app_name = 'sipanco.loginapp'

urlpatterns = [
    path('', views.index, name='index'),
]