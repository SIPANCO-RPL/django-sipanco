from typing import List, Optional
from django.http.request import HttpRequest
from django.shortcuts import redirect
from injector import inject

from app.auth.service import AuthService
from app.auth.models import Pasien, Petugas
from app.vaksin.models import JadwalVaksin, ReservasiVaksin
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

    def create_reservasi(self, request: HttpRequest) -> Optional[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Pasien):
            data = request.POST
            return self.vaksin_accessor.create_reservasi(data)

    def get_reservasi_list(self, request: HttpRequest) -> List[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            return self.vaksin_accessor.get_reservasi_vaksin(pasien_id=user.id)

        if isinstance(user, Petugas):
            # get rumah sakit dari petugas -> get reservasi vaksin dari jadwal yg ada di rumah sakit
            pass

        return self.vaksin_accessor.get_reservasi_vaksin()

    def create_vaksin(self, request: HttpRequest) -> Optional[JadwalVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Pasien):
            data = request.POST
            return self.vaksin_accessor.create_vaksin(data)

    def get_jadwal_list(self, request: HttpRequest) -> List[JadwalVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            return self.vaksin_accessor.get_jadwal_vaksin(pasien_id=user.id)

        if isinstance(user, Petugas):
            # get rumah sakit dari petugas -> get jadwal vaksin dari jadwal yg ada di rumah sakit
            pass

        return self.vaksin_accessor.get_jadwal_list()