from typing import List, Optional
from django.http.request import HttpRequest
from app.auth.models import Petugas, Pasien

from app.auth.service import AuthService
from app.rumah_sakit.models import Ruangan, RumahSakit
from app.rumah_sakit.accessor import RumahSakitAccessor, JadwalDokterAccessor, AppointmentDokterAccessor
from injector import inject
from app.rumah_sakit.models import JadwalDokter, AppointmentDokter


class RumahSakitService:
    @inject
    def __init__(self, auth_service: AuthService, rumah_sakit_accessor: RumahSakitAccessor, jadwal_dokter_accessor: JadwalDokterAccessor, appointment_dokter_accessor: AppointmentDokterAccessor) -> None:
        self.auth_service = auth_service
        self.rumah_sakit_accessor = rumah_sakit_accessor
        self.jadwal_dokter_accessor = jadwal_dokter_accessor
        self.appointment_dokter_accessor = appointment_dokter_accessor

    def create_ruangan(self, request: HttpRequest) -> Optional[Ruangan]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Petugas):
            ruangan = self.rumah_sakit_accessor.create_ruangan(request.POST["kode"], request.POST["kapasitas"], request.user.petugas.rumah_sakit)
            return ruangan
    
    def get_all_rumahsakit(self, request: HttpRequest) -> List[RumahSakit]:
        return self.rumah_sakit_accessor.get_all_rumahsakit()
    
    def get_rumah_sakit_by_id(self, num: int) -> Optional[RumahSakit]:
        return self.rumah_sakit_accessor.get_rumah_sakit_by_id(num)

    def get_all_ruangan(self, request: HttpRequest) -> List[Ruangan]:
        user = self.auth_service.get_user(request)

        if not user:
            return self.rumah_sakit_accessor.get_all_ruangan()
        
        if isinstance(user, Petugas):
            return self.rumah_sakit_accessor.get_ruangan_by_rumah_sakit(user.rumah_sakit)
        
        return self.rumah_sakit_accessor.get_all_ruangan()
    
    def create_jadwal_dokter(self, request: HttpRequest) -> Optional[JadwalDokter]:
        data_form = request.POST
        obj_rs = request.user.petugas.rumah_sakit
        new_jadwal = self.rumah_sakit_accessor.create_jadwal(data_form, obj_rs)
        return new_jadwal

    def create_appointment_dokter(self, request: HttpRequest, jadwaldokter_id: int) -> Optional[AppointmentDokter]:
        user = self.auth_service.get_user(request)

        if not isinstance(user, Pasien):
            return None

        jadwal = self.jadwal_dokter_accessor.get_by_id(jadwaldokter_id)
        data = {
            'jadwal_dokter': jadwal,
            'pasien': user,
            'keluhan': request.POST["keluhan"]
        }
        return self.appointment_dokter_accessor.create_appointment(data)
        

    def get_appointment_dokter(self, request: HttpRequest) -> List[AppointmentDokter]:
        user = self.auth_service.get_user(request)
        print("test")

        if isinstance(user, Pasien):
            return self.appointment_dokter_accessor.get_appointment_list(pasien_id=user.id)

        if isinstance(user, Petugas):
            return self.appointment_dokter_accessor.get_appointment_by_rumah_sakit(user.rumah_sakit)