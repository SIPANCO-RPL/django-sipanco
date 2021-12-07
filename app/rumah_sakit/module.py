from injector import Binder, Module, singleton
from .service import RumahSakitService
from .accessor import RumahSakitAccessor


class RumahSakitModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(RumahSakitService, to=RumahSakitService, scope=singleton)
        binder.bind(RumahSakitAccessor, to=RumahSakitAccessor, scope=singleton)
