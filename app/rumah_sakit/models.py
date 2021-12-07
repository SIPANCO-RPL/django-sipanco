from django.db import models
from django.db.models.deletion import CASCADE
from app.auth.models import Pasien

from app.auth.models import Petugas

class RumahSakit(models.Model):
    kode = models.CharField(max_length=64)
    nama = models.CharField(max_length=256, unique=True)
    alamat = models.CharField(max_length=512)
    kecamatan = models.CharField(max_length=256, null=True, default="Beji")
    kota = models.CharField(max_length=256, null=True, default="Depok")
    provinsi = models.CharField(max_length=256, null=True, default="Jawa Barat")
    kodepos = models.CharField(max_length=256, null=True, default="16424")
    petugas = models.OneToOneField(Petugas, on_delete=models.CASCADE, related_name="rumah_sakit", null=True)

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
    jadwal = models.DateTimeField(null=True)
    rumahsakit = models.ForeignKey(RumahSakit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.kode
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nama', 'jadwal', 'rumahsakit'], name='jadwal constraint')
        ]

class AppointmentDokter(models.Model):
    kode = models.CharField(max_length=64)
    keluhan = models.CharField(max_length=256)
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    jadwal_dokter = models.ForeignKey(JadwalDokter, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode
