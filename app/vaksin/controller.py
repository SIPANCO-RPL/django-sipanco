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
    return render(request, 'list-reservasi.html', {'reservasi_list': reservasi_list})


@methods(["GET", "POST"])
def create_reservasi_vaksin(request: HttpRequest):
    if request.method == "POST":
        reservasi = vaksin_service.create_reservasi(request)
        if not reservasi:
            context = {"message": "Gagal Membuat Reservasi"}
            return render(request, 'create_reservasi_vaksin.html', context)

        return reverse(list_reservasi_vaksin)

    return render(request, 'create_reservasi_vaksin.html')
