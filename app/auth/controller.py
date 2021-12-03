from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from app.di import injector
from .service import AuthService
from django.views.decorators.http import require_http_methods as methods


auth_service = injector.get(AuthService)

@methods(["GET"])
def index(request):
    return render(request, 'index.html')


@methods(["GET", "POST"])
def login(request: HttpRequest):
    if request.method == "POST":
        return auth_service.login(request)

    return auth_service.get_login(request)
