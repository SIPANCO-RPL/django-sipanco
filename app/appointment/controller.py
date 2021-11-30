from django.shortcuts import render
# from app.di import injector
# from .service import ILoginService, A
# from django.views.decorators.http import require_http_methods as methods


# login_service = injector.get(ILoginService)
# a = injector.get(A)

# @methods(["GET"])
def create_appointment(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'create_appointment.html')

def list_appointment(request):
    # print(login_service.test())
    # print(a.test())
    return render(request, 'list_appointment.html')