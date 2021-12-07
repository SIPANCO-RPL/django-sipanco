from django.db import models
from django.contrib.auth.models import User


class Pasien(User):
    nama = models.CharField(max_length=128)
    no_ktp = models.CharField(max_length=32)
    no_wa = models.CharField(max_length=16)
    bpjs = models.CharField(max_length=32)
    alamat = models.CharField(max_length=512)


class Petugas(User):
    nama = models.CharField(max_length=128)


class Admin(User):
    pass
