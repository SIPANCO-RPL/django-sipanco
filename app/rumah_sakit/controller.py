from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from app.di import injector
from django.views.decorators.http import require_http_methods as methods

from app.rumah_sakit.service import RumahSakitService

rumah_sakit_service = injector.get(RumahSakitService)

def lihat_rumah_sakit(request):
    return render(request, 'rumah_sakit.html')

def lihat_jadwal_dokter(request):
    return render(request, 'jadwal_dokter.html')

@methods(["GET"])
def lihat_ruangan(request: HttpRequest):
    context = {"list_ruangan": rumah_sakit_service.get_all_ruangan(request)}
    return render(request, 'list_ruangan.html', context)

def create_jadwal_dokter(request):
    return render(request, 'create_jadwal_dokter.html')

@methods(["GET", "POST"])
def create_ruangan(request: HttpRequest):
    if request.method == "POST":
        ruangan = rumah_sakit_service.create_ruangan(request)
        if ruangan:
            return redirect("/rumah-sakit/lihat-ruangan/")
       
        context = {"message": "Ruangan gagal dibuat"}
        return render(request, 'list_ruangan.html', context)

    return render(request, 'create_ruangan.html')

@methods(["GET"])
def list_appointment(request: HttpRequest):
    appointment_list = rumah_sakit_service.get_appointment_dokter(request)
    return render(request, 'list_appointment.html', {'appointment_list': appointment_list})

@methods(["GET", "POST"])
def create_appointment(request: HttpRequest):
    if request.method == "POST":
        reservasi = rumah_sakit_service.create_appointment_dokter(request)
        if not reservasi:
            context = {"message": "Gagal Membuat Reservasi"}
            return render(request, 'create_appointment.html', context)

        return reverse(list_appointment)

    return render(request, 'create_appointment.html')
