from typing import Optional, Union
from django.contrib.auth.models import User, auth
from django.http.request import HttpRequest
from injector import inject
from django.contrib.auth import logout

from app.auth.models import Pasien, Petugas

from .accessor import AuthAccessor


class AuthService:
    @inject
    def __init__(self, auth_accessor: AuthAccessor) -> None:
        self.auth_accessor = auth_accessor

    def login(self, request: HttpRequest, *args, **kwargs) -> Optional[User]:
        # Login sebagai Pasien
        username = request.POST['username']
        password = request.POST['password']

        tipe = kwargs.get('tipe', 'pasien')

        user = self.auth_accessor.authenticate(username, password, type=tipe)
        # user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user.user)
            request.session.set_expiry(3600) # auto logout dalam 1 Jam
            return user
        
        return None
    
    def register(self, request: HttpRequest) -> Optional[User]:
        try:
            user = self.auth_accessor.create_pasien(request.POST)
            return user
        except:
            pass
        
    def get_user(self, request: HttpRequest) -> Optional[Union[Pasien, Petugas]]:
        '''
        Get User Object based on the request, return None if not logged in
        '''
        user = request.user

        if user.is_superuser:
            return user

        if not user.is_authenticated:
            return None

        return getattr(user, 'petugas', None) or getattr(user, 'pasien', None)
    
    def logout(self, request: HttpRequest):
        logout(request)
