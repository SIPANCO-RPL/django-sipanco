from typing import List, Optional
from django.http.request import HttpRequest
from app.auth.models import Petugas

from app.auth.service import AuthService
from app.rumah_sakit.models import Ruangan
from app.rumah_sakit.accessor import RumahSakitAccessor
from injector import inject


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
        