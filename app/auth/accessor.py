from typing import Union, Optional
from django.contrib.auth.hashers import check_password

from .models import Pasien, Petugas, Admin


class AuthAccessor:
    def __init__(self) -> None:
        pass

    def _get_user_model(self, type: str = 'pasien') -> Optional[Union[Pasien, Petugas, Admin]]:
        if type == 'pasien':
            return Pasien
        if type == 'petugas':
            return Petugas
        if type == 'admin':
            return Admin

        return None

    def authenticate(
        self, username: str, password: str, type: str = "pasien"
    ) -> Optional[Union[Pasien, Petugas, Admin]]:

        user_model = self._get_user_model(type)

        if not user_model:
            return None

        user = user_model.objects.filter(username=username).first()

        if not user:
            return None
        
        if check_password(password, user.password):
            return user

        return None
    
    def get_user_by_id(self, user_id: str, type: str = "pasien") -> Optional[Union[Pasien, Petugas, Admin]]:
        user_model = self._get_user_model(type)

        if not user_model:
            return None

        return user_model.objects.filter(pk=user_id).first()
