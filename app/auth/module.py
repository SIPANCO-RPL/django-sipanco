from injector import Binder, Module, singleton
from .service import AuthService
from .accessor import AuthAccessor


class AuthModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AuthService, to=AuthService, scope=singleton)
        binder.bind(AuthAccessor, to=AuthAccessor, scope=singleton)
