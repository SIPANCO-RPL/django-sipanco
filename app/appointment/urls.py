from django.urls import path
from .controller import *

app_name = 'appointment'

urlpatterns = [
    path('createappointment', create_appointment, name='create_appointment'),
    path('', list_appointment, name='list_appointment'),
]
