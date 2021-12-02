from injector import Injector
from app.auth.module import AuthModule
from app.appointment.module import AppointmentModule
from app.rumah_sakit.module import RumahSakitModule
from app.vaksin.module import VaksinModule

injector = Injector([
    AuthModule,
    AppointmentModule,
    RumahSakitModule,
    VaksinModule,
])
