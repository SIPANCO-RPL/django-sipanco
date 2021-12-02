from django.db import models
from django.contrib.auth.models import User


class Pasien(User):
    no_ktp = models.CharField(max_length=50)
    no_wa = models.CharField(max_length=15)
