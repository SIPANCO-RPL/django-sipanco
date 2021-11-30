from django.urls import path
from .controller import *

app_name = 'rumah_sakit'

urlpatterns = [
    path('', lihat_rumah_sakit, name='lihat_rumah_sakit'),
    path('create', lihat_rumah_sakit, name='lihat_rumah_sakit'),
]
