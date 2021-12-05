from django.db import models
from django.db.models.deletion import CASCADE
from app.auth.models import Pasien

class RumahSakit(models.Model):
    kode = models.CharField(max_length=64)
    nama = models.CharField(max_length=256)
    alamat = models.CharField(max_length=512)

    def __str__(self):
        return self.nama

class Ruangan(models.Model):
    kode = models.CharField(max_length=64)
    kapasitas = models.PositiveIntegerField()
    kapasitasTergunakan = models.PositiveIntegerField()
    rumahSakit = models.ForeignKey(RumahSakit, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode

class JadwalDokter(models.Model):
    kode = models.CharField(max_length=64)
    nama = models.CharField(max_length=256)
    spesialis = models.CharField(max_length=512)
    jadwal = models.CharField(max_length=512)

    def __str__(self):
        return self.nama

class Apppointment(models.Model):
    kode = models.CharField(max_length=64)
    keluhan = models.CharField(max_length=256)
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    jadwal_dokter = models.ForeignKey(JadwalDokter, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode
