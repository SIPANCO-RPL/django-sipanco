# Generated by Django 3.2.9 on 2021-12-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_reservasivaksin_status'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ruangan',
            constraint=models.UniqueConstraint(fields=('kode', 'rumahSakit'), name='ruangan constraint'),
        ),
    ]