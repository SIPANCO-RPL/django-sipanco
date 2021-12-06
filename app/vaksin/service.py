from typing import List, Optional
from django.http.request import HttpRequest
from django.shortcuts import redirect
from injector import inject
import random
import string

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
            jadwal = self.jadwal_vaksin_accessor.get_by_id(request.POST['jadwal_id'])

            if jadwal.reservasi_vaksin_set.count() >= jadwal.kuota:
                return None

            kode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            kode = f"{kode}_{jadwal.id}_{jadwal.kuota_terisi}"
            data = {
                'jadwal_vaksin': jadwal,
                'pasien': user,
                'selesai': False,
                'vaksin_ke': user.jml_vaksin + 1,
                'kode': kode
            }
            return self.reservasi_vaksin_accessor.create(data)


    def get_reservasi_list(self, request: HttpRequest) -> List[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if user.is_superuser:
            return self.reservasi_vaksin_accessor.get_reservasi_vaksin()

        if isinstance(user, Pasien):
            return self.reservasi_vaksin_accessor.get_reservasi_vaksin(pasien_id=user.id)

        if isinstance(user, Petugas):
            # jadwal = self.jadwal_vaksin_accessor.get_by_rs(user.rumah_sakit.id)
            rs_id = user.rumah_sakit.id
            return self.reservasi_vaksin_accessor.get_reservasi_vaksin(rs_id=rs_id)

        return []
