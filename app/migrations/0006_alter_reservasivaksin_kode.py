# Generated by Django 3.2.9 on 2021-12-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_reservasivaksin_vaksin_ke'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasivaksin',
            name='kode',
            field=models.CharField(default='NO_CODE', max_length=32),
        ),
    ]
