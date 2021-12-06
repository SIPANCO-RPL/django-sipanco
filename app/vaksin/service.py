from typing import List, Optional
from django.http.request import HttpRequest
from django.shortcuts import redirect
from injector import inject

from app.auth.service import AuthService
from app.auth.models import Pasien, Petugas
from app.vaksin.models import JadwalVaksin, ReservasiVaksin
from .accessor import ReservasiVaksinAccessor, JadwalVaksinAccessor

class VaksinService:
    @inject
    def __init__(
        self,
        vaksin_accessor: ReservasiVaksinAccessor,
        jadwal_vaksin_accessor: JadwalVaksinAccessor,
        auth_service: AuthService,
    ) -> None:
        self.reservasi_vaksin_accessor = vaksin_accessor
        self.auth_service = auth_service
        self.jadwal_vaksin_accessor = jadwal_vaksin_accessor

    def create_reservasi(self, request: HttpRequest) -> Optional[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Pasien):
            data = request.POST
            return self.reservasi_vaksin_accessor.create_reservasi(data)
        


    def get_reservasi_list(self, request: HttpRequest) -> List[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            return self.reservasi_vaksin_accessor.get_reservasi_vaksin(pasien_id=user.id)

        if isinstance(user, Petugas):
            # jadwal = self.jadwal_vaksin_accessor.get_by_rs(user.rumah_sakit.id)
            rs_id = user.rumah_sakit.id
            return self.reservasi_vaksin_accessor.get_reservasi_vaksin(rs_id=rs_id)

        return self.reservasi_vaksin_accessor.get_reservasi_vaksin()

        
