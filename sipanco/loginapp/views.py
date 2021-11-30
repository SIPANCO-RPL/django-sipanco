from django.shortcuts import render
from sipanco.di import injector
from .service import ILoginService
from django.views.decorators.http import require_http_methods as methods


login_service = injector.get(ILoginService)

@methods(["GET"])
def index(request):
    print(login_service.test())
    return render(request, 'index.html')
