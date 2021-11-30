from injector import Binder, Module, singleton
from .service import LoginService, ILoginService


class LoginModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ILoginService, to=LoginService, scope=singleton)
