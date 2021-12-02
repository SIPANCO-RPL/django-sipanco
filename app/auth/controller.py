from django.shortcuts import render
from app.di import injector
from .service import AuthService
from django.views.decorators.http import require_http_methods as methods


login_service = injector.get(AuthService)

@methods(["GET"])
def index(request):
    print(login_service.test())
    return render(request, 'index.html')
