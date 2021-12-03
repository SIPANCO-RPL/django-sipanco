from typing import Optional
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from injector import inject

from .accessor import AuthAccessor


class AuthService:
    @inject
    def __init__(self, auth_accessor: AuthAccessor) -> None:
        self.auth_accessor = auth_accessor

    def login(self, request: HttpRequest) -> Optional[User]:
        pass

    def get_user(self, request: HttpRequest) -> Optional[User]:
        '''
        Get User Object based on the request, return None if not logged in
        '''
        return None
