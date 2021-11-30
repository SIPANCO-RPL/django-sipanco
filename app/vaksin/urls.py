from django.urls import path
from .controller import *

app_name = 'vaksin'

urlpatterns = [
    path('/addVaksin', create_vaksin, name='create_vaksin'),
    path('/showVaksin', list_vaksin, name='list_vaksin'),
]
