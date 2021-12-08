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

    def _cek_jumlah_reservasi(
        self,
        pasien_id: Optional[int] = None,
        jadwal_id: Optional[int] = None,
    ) -> int:
        return len(list(self.reservasi_vaksin_accessor.get_valid(pasien_id=pasien_id, jadwal_id=jadwal_id)))

    def create_reservasi(self, request: HttpRequest, jadwal_id: int) -> Optional[ReservasiVaksin]:
        user = self.auth_service.get_user(request)

        if not isinstance(user, Pasien):
            return None

        if self._cek_jumlah_reservasi(pasien_id=user.id) >= Pasien.MAX_VAKSIN:
            return None

        jadwal = self.jadwal_vaksin_accessor.get_by_id(jadwal_id)
        kuota_terisi = self._cek_jumlah_reservasi(jadwal_id=jadwal_id)

        if kuota_terisi >= jadwal.kuota or self._cek_jumlah_reservasi(pasien_id=user.id, jadwal_id=jadwal_id) >= 1:
            return None

        kode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        kode = f"{user.id}_{kode}_{jadwal.id}_{kuota_terisi + 1}"
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

        if self._cek_jumlah_reservasi(pasien_id=user.id) >= 2:
            return {"success": False, "message": "Kamu memiliki reservasi lebih dari 2"}

        jadwal = self.jadwal_vaksin_accessor.get_by_id(jadwal_id)

        if not jadwal:
            return {"success": False, "message": "Jadwal yang kamu pilih tidak valid"}

        if self._cek_jumlah_reservasi(jadwal_id=jadwal_id) >= jadwal.kuota:
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
            return self.reservasi_vaksin_accessor.get_list(pasien_id=user.id)

        if isinstance(user, Petugas):
            # jadwal = self.jadwal_vaksin_accessor.get_by_rs(user.rumah_sakit.id)
            rs_id = user.rumah_sakit.id
            return self.reservasi_vaksin_accessor.get_list(rs_id=rs_id)

        return []

    def create_vaksin(self, request: HttpRequest) -> Optional[JadwalVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Petugas):
            jadwalVaksin = self.jadwal_vaksin_accessor.create_vaksin(request.POST["tanggal"], request.POST["waktu"], request.POST["kuota"], request.user.petugas.rumah_sakit)
            return jadwalVaksin

    def get_all_vaksin(self, request: HttpRequest) -> List[JadwalVaksin]:
        user = self.auth_service.get_user(request)

        if not user:
            return self.jadwal_vaksin_accessor.get_all_jadwalVaksin()

        if isinstance(user, Petugas):
            return self.jadwal_vaksin_accessor.get_all_jadwalVaksin()

        return self.jadwal_vaksin_accessor.get_all_jadwalVaksin()