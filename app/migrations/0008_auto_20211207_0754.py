# Generated by Django 3.2.9 on 2021-12-07 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211207_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwaldokter',
            name='rumahsakit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.rumahsakit'),
        ),
        migrations.AlterField(
            model_name='jadwaldokter',
            name='jadwal',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rumahsakit',
            name='nama',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AddConstraint(
            model_name='jadwaldokter',
            constraint=models.UniqueConstraint(fields=('nama', 'jadwal', 'rumahsakit'), name='jadwal constraint'),
        ),
    ]