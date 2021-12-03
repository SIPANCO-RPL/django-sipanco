from typing import Optional
from django.contrib.auth.models import User, auth
from django.http.request import HttpRequest
from injector import inject
from django.shortcuts import redirect

from .accessor import AuthAccessor


class AuthService:
    @inject
    def __init__(self, auth_accessor: AuthAccessor) -> None:
        self.auth_accessor = auth_accessor

    def login(self, request: HttpRequest) -> Optional[User]:
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(300) # auto logout dalam 5 menit
            return redirect('/')


    def get_user(self, request: HttpRequest) -> Optional[User]:
        '''
        Get User Object based on the request, return None if not logged in
        '''
        return None
