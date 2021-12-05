# Generated by Django 3.2.9 on 2021-12-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211204_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=64)),
                ('kapasitas', models.PositiveIntegerField()),
                ('kapasitasTergunakan', models.PositiveIntegerField()),
                ('rumahSakit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rumahsakit')),
            ],
        ),
        migrations.AddField(
            model_name='petugas',
            name='rumah_sakit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petugas_rs', to='app.rumahsakit'),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]