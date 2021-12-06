from django.db import models
from django.contrib.auth.models import User
from app.rumah_sakit.models import RumahSakit


class Pasien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pasien")
    nama = models.CharField(max_length=128, null=False)
    no_ktp = models.CharField(max_length=32, default="")
    no_wa = models.CharField(max_length=16, default="")
    bpjs = models.CharField(max_length=32, default="")
    alamat = models.CharField(max_length=512, default="")
    jml_vaksin = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama

    class Meta(type):
        ordering = ('nama', )


class Petugas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="petugas")
    rumah_sakit = models.OneToOneField(RumahSakit, on_delete=models.CASCADE, related_name="petugas_rs", null=True)
    nama = models.CharField(max_length=128)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ('nama', )
