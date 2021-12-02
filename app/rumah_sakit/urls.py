from django.urls import path
from .controller import *

app_name = 'rumah_sakit'

urlpatterns = [
    path('', lihat_rumah_sakit, name='lihat_rumah_sakit'),
    path('rsui', lihat_jadwal_dokter, name='lihat_jadwal_dokter'),
    path('create-jadwal', create_jadwal_dokter, name='create_jadwal_dokter'),
    path('lihat-ruangan', lihat_ruangan, name='lihat_ruangan'),
    path('buat-ruangan', create_ruangan, name="buat_ruangan"),
    path('createappointment', create_appointment, name='create_appointment'),
    path('listappointment', list_appointment, name='list_appointment'),
]
