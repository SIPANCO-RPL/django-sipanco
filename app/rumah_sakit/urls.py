from django.urls import path
from .controller import *

app_name = 'rumah_sakit'

urlpatterns = [
    path('', lihat_rumah_sakit, name='lihat_rumah_sakit'),
    path('/rsui', lihat_jadwal_dokter, name='lihat_jadwal_dokter'),
    path('/create-jadwal', create_jadwal_dokter, name='create_jadwal_dokter'),
]
