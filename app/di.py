from injector import Injector
from app.auth.module import AuthModule

injector = Injector([
    AuthModule
])
