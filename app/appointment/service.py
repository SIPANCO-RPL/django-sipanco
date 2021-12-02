from django.http.request import HttpRequest
from injector import inject


class AppointmentService:
    @inject
    def __init__(self) -> None:
        pass

    def aaa(self, request: HttpRequest):
        a = request.method
        pass

    def test(self) -> str:
        return "test success"
