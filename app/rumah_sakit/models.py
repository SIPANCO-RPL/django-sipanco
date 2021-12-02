from django.db import models

class RumahSakit(models.Model):
    kode = models.CharField(max_length=64)
    nama = models.CharField(max_length=256)
    alamat = models.CharField(max_length=512)
