from django.contrib import admin

from app.vaksin.models import *
from app.auth.models import *
from app.rumah_sakit.models import *
# Register your models here.

admin.site.register(Pasien)
admin.site.register(Petugas)
admin.site.register(RumahSakit)
admin.site.register(Ruangan)
admin.site.register(JadwalDokter)
admin.site.register(JadwalVaksin)
admin.site.register(ReservasiVaksin)
admin.site.register(AppointmentDokter)