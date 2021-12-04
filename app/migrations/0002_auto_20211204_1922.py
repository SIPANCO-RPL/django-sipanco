# Generated by Django 3.2.9 on 2021-12-04 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='alamat',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='bpjs',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='jml_vaksin',
            field=models.PositiveIntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='no_ktp',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='no_wa',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='pasien',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pasien', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='petugas',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='petugas', to=settings.AUTH_USER_MODEL),
        ),
    ]