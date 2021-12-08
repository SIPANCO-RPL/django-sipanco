from django.db import models
from app.auth.models import Pasien
from app.rumah_sakit.models import RumahSakit


class JadwalVaksin(models.Model):
    tanggal = models.DateField(null=True)
    waktu = models.TimeField(null=True)
    kuota = models.PositiveIntegerField()
    rumah_sakit = models.ForeignKey(RumahSakit, on_delete=models.CASCADE)


class ReservasiVaksin(models.Model):

    class StatusEnum(models.TextChoices):
        SELESAI = "SELESAI"
        TERDAFTAR = "TERDAFTAR"
        BATAL = "BATAL"


    kode = models.CharField(max_length=32, default='NO_CODE')
    vaksin_ke = models.SmallIntegerField(default=0)
    status = models.CharField(
        max_length=32,
        choices=StatusEnum.choices,
        default=StatusEnum.BATAL,
    )
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    jadwal_vaksin = models.ForeignKey(JadwalVaksin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kode} - {self.pasien.nama}"
