from injector import Binder, Module, singleton
from .service import VaksinService
from .accessor import ReservasiVaksinAccessor, JadwalVaksinAccessor


class VaksinModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(VaksinService, to=VaksinService, scope=singleton)
        binder.bind(ReservasiVaksinAccessor, to=ReservasiVaksinAccessor, scope=singleton)
        binder.bind(JadwalVaksinAccessor, to=JadwalVaksinAccessor, scope=singleton)
