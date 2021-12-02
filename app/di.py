from injector import Injector
from app.auth.module import AuthModule
from app.rumah_sakit.module import RumahSakitModule
from app.vaksin.module import VaksinModule

injector = Injector([
    AuthModule,
    RumahSakitModule,
    VaksinModule,
])
