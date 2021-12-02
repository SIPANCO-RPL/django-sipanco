from injector import Binder, Module, singleton
from .service import AppointmentService
from .accessor import AppointmentAccessor


class AppointmentModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AppointmentService, to=AppointmentService, scope=singleton)
        binder.bind(AppointmentAccessor, to=AppointmentAccessor, scope=singleton)
