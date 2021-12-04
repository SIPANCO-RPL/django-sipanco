from django.db import models
from django.contrib.auth.models import User


class Pasien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=128)
    no_ktp = models.CharField(max_length=32)
    no_wa = models.CharField(max_length=16)
    bpjs = models.CharField(max_length=32)
    alamat = models.CharField(max_length=512)
    jml_vaksin = models.PositiveIntegerField(max_length=2)

    class Meta(type):
        ordering = ('nama', )
        # def __str__(self):
        #     return nama


class Petugas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=128)

    class Meta:
        ordering = ('nama', )
        # def __str__(self):
        #     return nama


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=128)

    class Meta:
        ordering = ('nama', )
