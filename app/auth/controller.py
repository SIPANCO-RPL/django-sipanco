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
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        user = auth_service.login(request)
        if user is not None:
            return redirect("/")
        
        return render(request, "login/login.html", {"error_message": "Password / Username Salah"})

    return render(request, "login/login.html")

@methods(["GET"])
def logout(request: HttpRequest):
    if request.user.is_authenticated:
        auth_service.logout(request)
        return redirect("/")

@methods(["GET", "POST"])
def register_pasien(request: HttpRequest):
    if request.method == "POST":
        user = auth_service.register(request)
        if (user is not None):
            return render(request, "register/register.html", {"created_user": user})
        
        return render(request, "register/register.html", {"error_message": "terjadi error"})
    
    return render(request, "register/register.html")

@methods(["GET", "POST"])
def login_petugas(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        user = auth_service.login(request, tipe="petugas")
        if user is not None:
            return redirect("/")

    return render(request, "login/login_petugas.html")
