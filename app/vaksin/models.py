from django.db import models
from django import forms

from app.auth.models import Pasien
from app.rumah_sakit.models import RumahSakit


class JadwalVaksin(models.Model):
    tanggal = models.DateField()
    waktu = models.TimeField()
    kuota = models.PositiveIntegerField()
    rumah_sakit = models.ForeignKey(RumahSakit, on_delete=models.CASCADE)


class ReservasiVaksin(models.Model):
    kode = models.CharField(max_length=32)
    vaksin_ke = models.SmallIntegerField(max_length=3)
    selesai = models.BooleanField(default=False)
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    jadwal_vaksin = models.ForeignKey(JadwalVaksin, on_delete=models.CASCADE)
