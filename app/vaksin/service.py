from typing import List
from django.http.request import HttpRequest
from django.shortcuts import redirect
from injector import inject

from app.auth.service import AuthService
from app.auth.models import Pasien
from app.vaksin.models import JadwalVaksin
from .accessor import VaksinAccessor

class VaksinService:
    @inject
    def __init__(
        self,
        vaksin_accessor: VaksinAccessor,
        auth_service: AuthService,
    ) -> None:
        self.vaksin_accessor = vaksin_accessor
        self.auth_service = auth_service

    def create_vaksin(self, request: HttpRequest):
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            pass

    def create_reservasi(self, request: HttpRequest):
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            pass

    def get_reservasi(self, request: HttpRequest):
        # jadwal_vaksin: List[JadwalVaksin] = self.rumah_sakit_accessor.get_jadwal_vaksin(rs_id)
        pass

