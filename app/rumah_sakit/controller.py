from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from app.di import injector
from django.views.decorators.http import require_http_methods as methods

from app.rumah_sakit.service import RumahSakitService

rumah_sakit_service = injector.get(RumahSakitService)

@methods(["GET"])
def lihat_rumah_sakit(request):
    context = {"list_rumah_sakit": rumah_sakit_service.get_all_rumahsakit(request)}
    return render(request, 'rumah_sakit/rumah_sakit.html', context)

@methods(["GET"])
def detail_rumah_sakit(request, num: int):
    mod_number = num % 5
    detail_data = rumah_sakit_service.get_rumah_sakit_by_id(num)
    
    context = {"mod_number": mod_number, "detail_data": detail_data}
    return render(request, 'rumah_sakit/detail_rumah_sakit.html', context)

@methods(["GET"])
def lihat_ruangan(request: HttpRequest):
    context = {"list_ruangan": rumah_sakit_service.get_all_ruangan(request)}
    return render(request, 'list_ruangan.html', context)

@methods(["GET", "POST"])
def create_jadwal_dokter(request):  
        if not request.user.is_authenticated:
            return redirect("/")

        if request.user.petugas is None:
            return redirect("/")

        if request.method == "POST":
            jadwal_baru = rumah_sakit_service.create_jadwal_dokter(request)
            if jadwal_baru is not None:
                return render(request, 'rumah_sakit/create_jadwal_dokter.html', {"success": "success"})
            
            return render(request, 'rumah_sakit/create_jadwal_dokter.html', {"failed": "failed"})
        
        return render(request, 'rumah_sakit/create_jadwal_dokter.html')

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
