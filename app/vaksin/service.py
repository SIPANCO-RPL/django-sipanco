from django.http.request import HttpRequest
from injector import inject

from .accessor import VaksinAccessor

class VaksinService:
    @inject
    def __init__(self, vaksin_accessor: VaksinAccessor) -> None:
        self.vaksin_accessor = vaksin_accessor

    def create_reservasi(self, request: HttpRequest):
        pass

    def get_reservasi(self, request: HttpRequest):
        pass
