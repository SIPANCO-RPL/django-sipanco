from django.db import models
from django.db.models.deletion import CASCADE

class RumahSakit(models.Model):
    kode = models.CharField(max_length=64, primary_key=True)
    nama = models.CharField(max_length=256)
    alamat = models.CharField(max_length=512)

    def __str__(self):
        return self.nama

class Ruangan(models.Model):
    kode = models.CharField(max_length=64, primary_key=True)
    kapasitas = models.PositiveIntegerField()
    kapasitasTergunakan = models.PositiveIntegerField()
    rumahSakit = models.ForeignKey(RumahSakit, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode
