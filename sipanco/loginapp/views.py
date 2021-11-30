from django.shortcuts import render
from sipanco.di import injector
from .service import ILoginService

login_service = injector.get(ILoginService)

def index(request):
    print(login_service.test())
    return render(request, 'index.html')
