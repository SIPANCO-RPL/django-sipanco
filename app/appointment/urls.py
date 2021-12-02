from django.urls import path
from .controller import *

app_name = 'appointment'

urlpatterns = [
    path('create', create_appointment, name='create_appointment'),
    path('list', list_appointment, name='list_appointment'),
]
