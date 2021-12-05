from typing import List, Optional
from django.http.request import HttpRequest
from app.auth.models import Petugas, Pasien

from app.auth.service import AuthService
from app.rumah_sakit.models import Ruangan
from app.rumah_sakit.accessor import RumahSakitAccessor
from injector import inject
from app.rumah_sakit.models import JadwalDokter, AppointmentDokter


class RumahSakitService:
    @inject
    def __init__(self, auth_service: AuthService, rumah_sakit_accessor: RumahSakitAccessor) -> None:
        self.auth_service = auth_service
        self.rumah_sakit_accessor = rumah_sakit_accessor
    
    def create_ruangan(self, request: HttpRequest) -> Optional[Ruangan]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Petugas):
            return self.rumah_sakit_accessor.create_ruangan(request.POST["kodeRuangan"], request.POST["kapastias"])

    def get_all_ruangan(self, request: HttpRequest) -> List[Ruangan]:
        user = self.auth_service.get_user(request)

        if not user:
            return self.rumah_sakit_accessor.get_all_ruangan()
        
        if isinstance(user, Petugas):
            #return self.rumah_sakit_accessor.get_ruangan_by_petugas(user.get_rumah_sakit)
            pass
        
        return self.rumah_sakit_accessor.get_all_ruangan()

    def create_appointment_dokter(self, request: HttpRequest) -> Optional[AppointmentDokter]:
        user = self.auth_service.get_user(request)

        if not user:
            return None

        if isinstance(user, Pasien):
            data = request.POST
            return self.rumah_sakit_accessor.create_appointment(data)
        

    def get_appointment_dokter(self, request: HttpRequest) -> List[AppointmentDokter]:
        user = self.auth_service.get_user(request)

        if not user:
            return redirect('/')

        if isinstance(user, Pasien):
            return self.rumah_sakit_accessor.get_appointment_dokter(pasien_id=user.id)

        if isinstance(user, Petugas):
            # get rumah sakit dari petugas -> get reservasi vaksin dari jadwal yg ada di rumah sakit
            pass

        return self.rumah_sakit_accessor.get_appointment_dokter()
        