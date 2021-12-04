from django.contrib import admin
from .auth.models import *
from .rumah_sakit.models import *
# Register your models here.

admin.site.register(Pasien)
admin.site.register(Petugas)
admin.site.register(RumahSakit)
admin.site.register(Ruangan)