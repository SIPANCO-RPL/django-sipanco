from injector import Binder, Module, singleton
from .service import VaksinService
from .accessor import VaksinAccessor


class VaksinModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(VaksinService, to=VaksinService, scope=singleton)
        binder.bind(VaksinAccessor, to=VaksinAccessor, scope=singleton)
