from django.http.request import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods as methods

from app.rumah_sakit.service import RumahSakitService


def lihat_rumah_sakit(request):
    return render(request, 'rumah_sakit.html')

def lihat_jadwal_dokter(request):
    return render(request, 'jadwal_dokter.html')

@methods(["GET"])
def lihat_ruangan(request: HttpRequest):
    context = {"list_ruangan": RumahSakitService.get_all_ruangan(request)}
    return render(request, 'list_ruangan.html')

def create_jadwal_dokter(request):
    return render(request, 'create_jadwal_dokter.html')

@methods(["GET", "POST"])
def create_ruangan(request: HttpRequest):
    if request.method == "POST":
        ruangan = RumahSakitService.create_ruangan(request)
        if not ruangan:
            context = {"message": "Ruangan gagal dibuat"}
            return render(request, 'list_ruangan.html', context)

        return reverse(lihat_ruangan)

    return render(request, 'create_ruangan.html')

@methods(["GET"])
def list_appointment(request: HttpRequest):
    appointment_list = RumahSakitService.get_appointment_dokter(request)
    return render(request, 'list_appointment.html', {'appointment_list': appointment_list})

@methods(["GET", "POST"])
def create_appointment(request: HttpRequest):
    if request.method == "POST":
        reservasi = RumahSakitService.create_appointment_dokter(request)
        if not reservasi:
            context = {"message": "Gagal Membuat Reservasi"}
            return render(request, 'create_appointment.html', context)

        return reverse(list_appointment)

    return render(request, 'create_appointment.html')
