from django.db import models
from app.auth.models import Pasien

class JadwalVaksin(models.Model):
    waktu = models.DateTimeField()
    kuota = models.PositiveIntegerField()


class ReservasiVaksin(models.Model):
    kode = models.CharField(max_length=32)
    vaksin_ke = models.SmallIntegerField(max_length=3)
    pasien = models.ForeignKey(Pasien)
    jadwal_vaksin = models.ForeignKey(JadwalVaksin)
