from django.urls import path
from .controller import *

app_name = 'vaksin'

urlpatterns = [
    path('', list_vaksin, name='list_vaksin'),
    path('addVaksin', create_vaksin, name='create_vaksin'),
    path('reservasi/list', list_reservasi_vaksin, name='list_reservasi_vaksin'),
    path('reservasi/create', create_reservasi_vaksin, name='create_reservasi_vaksin'),
]
