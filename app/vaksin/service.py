from typing import Any, Dict, List, Optional
from django.http.request import HttpRequest
from django.shortcuts import redirect
from injector import inject
import random
import string

from app.auth.service import AuthService
from app.auth.models import Pasien, Petugas
from app.rumah_sakit.models import RumahSakit
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

    def _cek_jumlah_reservasi(self, pasien: Pasien) -> int:
        return len(list(self.reservasi_vaksin_accessor.get_valid_by_pasien(pasien.id)))

    def create_reservasi(self, request: HttpRequest, jadwal_id: int) -> Optional[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not isinstance(user, Pasien):
            return None

        if self._cek_jumlah_reservasi(user) >= Pasien.MAX_VAKSIN:
            return None

        jadwal = self.jadwal_vaksin_accessor.get_by_id(jadwal_id)
        kuota = jadwal.reservasivaksin_set.count()

        if kuota >= jadwal.kuota:
            return None

        kode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        kode = f"{kode}_{jadwal.id}_{jadwal.kuota + 1}"
        data = {
            'jadwal_vaksin': jadwal,
            'pasien': user,
            'status': "TERDAFTAR",
            'vaksin_ke': user.jml_vaksin + 1,
            'kode': kode
        }
        return self.reservasi_vaksin_accessor.create(data)

    def get_create_reservasi(self, request: HttpRequest, jadwal_id: int) -> Dict[str, Any]:
        user = self.auth_service.get_user(request)

        if not isinstance(user, Pasien):
            return {"success": False, "message": "Kamu tidak bisa membuat reservasi"}

        if self._cek_jumlah_reservasi(user) >= 2:
            return {"success": False, "message": "Kamu memiliki reservasi lebih dari 2"}

        jadwal = self.jadwal_vaksin_accessor.get_by_id(jadwal_id)

        if jadwal.reservasivaksin_set.count() >= jadwal.kuota:
            return {"success": False, "message": "Kuota sudah penuh"}

        rumah_sakit: RumahSakit = jadwal.rumah_sakit

        return {
            "success": True,
            "rumah_sakit": rumah_sakit,
            "jadwal": jadwal,
        }



    def get_reservasi_list(self, request: HttpRequest) -> List[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if getattr(user, "is_superuser", None):
            return self.reservasi_vaksin_accessor.get_list()

        if isinstance(user, Pasien):
            print(user)
            return self.reservasi_vaksin_accessor.get_list(pasien_id=user.id)

        if isinstance(user, Petugas):
            # jadwal = self.jadwal_vaksin_accessor.get_by_rs(user.rumah_sakit.id)
            rs_id = user.rumah_sakit.id
            return self.reservasi_vaksin_accessor.get_list(rs_id=rs_id)

        return []
