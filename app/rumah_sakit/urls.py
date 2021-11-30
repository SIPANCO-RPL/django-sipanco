from django.urls import path
from .controller import *

app_name = 'auth'

urlpatterns = [
    path('', lihat_rumah_sakit, name='lihat_rumah_sakit'),
]
