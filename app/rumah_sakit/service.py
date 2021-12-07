from django.http.request import HttpRequest
from injector import inject


class RumahSakitService:
    @inject
    def __init__(self) -> None:
        pass

    def login(self, request: HttpRequest):
        a = request.method
        pass

    def test(self) -> str:
        return "test success"
