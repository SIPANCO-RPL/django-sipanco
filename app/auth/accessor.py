from typing import Union, Optional
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import Pasien, Petugas


class AuthAccessor:
    def __init__(self) -> None:
        pass

    def _get_user_model(self, type: str = 'pasien') -> Optional[Union[Pasien, Petugas]]:
        if type == 'pasien':
            return Pasien
        if type == 'petugas':
            return Petugas

        return None

    def authenticate(
        self, username: str, password: str, type: str = "pasien"
    ) -> Optional[Union[Pasien, Petugas]]:

        user_model = self._get_user_model(type)

        if not user_model:
            return None

        user = user_model.objects.filter(user__username=username).first()

        if not user:
            return None

        if check_password(password, user.user.password):
            return user

        return None

    def get_user_by_id(self, user_id: str, type: str = "pasien") -> Optional[Union[Pasien, Petugas]]:
        user_model = self._get_user_model(type)

        if not user_model:
            return None

        try:
            return user_model.objects.get(pk=user_id)
        except:
            return None

    def create_pasien(self, dict_data: dict) -> Optional[Pasien]:
        try:
            new_user = User.objects.create_user(
                username=dict_data["name"], password=dict_data["password"])
            new_user.save()

            user = Pasien(user=new_user, nama=dict_data["name"], no_ktp=dict_data["no_ktp"],
                          no_wa=dict_data["no_wa"], bpjs=dict_data["bpjs"], alamat=dict_data["alamat"])
            user.save()

            return user
        except:
            return None
