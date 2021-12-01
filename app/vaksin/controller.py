from django.http.request import HttpRequest
from django.shortcuts import render
# from app.di import injector
# from .service import ILoginService, A
# from django.views.decorators.http import require_http_methods as methods


# login_service = injector.get(ILoginService)
# a = injector.get(A)

# @methods(["GET"])
def create_vaksin(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'addVaksin.html')

def list_vaksin(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'showVaksin.html')

def list_reservasi_vaksin(request: HttpRequest):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'list-reservasi.html')

def create_reservasi_vaksin(request: HttpRequest):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'create_reservasi_vaksin.html')
