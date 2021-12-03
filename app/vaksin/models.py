from django.db import models
from django import forms

from app.auth.models import Pasien
from app.rumah_sakit.models import RumahSakit


class JadwalVaksin(models.Model):
    waktu = models.DateTimeField()
    kuota = models.PositiveIntegerField()
    rumah_sakit = models.ForeignKey(RumahSakit)


class ReservasiVaksin(models.Model):
    kode = models.CharField(max_length=32)
    vaksin_ke = models.SmallIntegerField(max_length=3)
    selesai = models.BooleanField(default=False)
    pasien = models.ForeignKey(Pasien)
    jadwal_vaksin = models.ForeignKey(JadwalVaksin)


class CreateReservasiVaksin(forms.Form):
    kode = models.CharField(max_length=32)

