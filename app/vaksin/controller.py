from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods as methods

from app.di import injector
from .service import VaksinService


vaksin_service = injector.get(VaksinService)

@methods(["GET"])
def create_vaksin(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'addVaksin.html')


def list_vaksin(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'showVaksin.html')


@methods(["GET"])
def list_reservasi_vaksin(request: HttpRequest):
    reservasi_list = vaksin_service.get_reservasi_list(request)
    print(reservasi_list)
    return render(request, 'list-reservasi.html', {'reservasi_list': reservasi_list})


@methods(["GET", "POST"])
def create_reservasi_vaksin(request: HttpRequest, jadwal_id: int):

    context = {
        "data": None,
        "is_valid": False,
        "success": False,
        "message": "",
    }
    if request.method == "POST":
        reservasi = vaksin_service.create_reservasi(request, jadwal_id)
        if not reservasi:
            context["message"] = "Gagal Membuat Reservasi, Kamu tidak bisa atau kuota sudah penuh"
            context["success"] = False

            return render(request, 'create_reservasi_vaksin.html', context)

        context["message"] = "Sukses Membuat Reservasi"
        context["success"] = True
        return render(request, 'create_reservasi_vaksin.html', context)
    
    data = vaksin_service.get_create_reservasi(request, jadwal_id)
    context['data'] = data
    context['is_get'] = True

    return render(request, 'create_reservasi_vaksin.html', context)
