from django.http.request import HttpRequest
from django.shortcuts import render
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
    # print(login_service.test())
    # print(a.test())
    return render(request, 'list-reservasi.html')

@methods(["GET", "POST"])
def create_reservasi_vaksin(request: HttpRequest):
    

    return render(request, 'create_reservasi_vaksin.html')
