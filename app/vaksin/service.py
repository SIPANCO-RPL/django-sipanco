from django.http.request import HttpRequest
from injector import inject

from .accessor import VaksinAccessor

class VaksinService:
    @inject
    def __init__(self, vaksin_accessor: VaksinAccessor) -> None:
        self.vaksin_accessor = vaksin_accessor

    def login(self, request: HttpRequest):
        a = request.method
        pass

    def test(self) -> str:
        return "test success"
