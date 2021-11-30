from abc import ABC, abstractmethod
from django.http.request import HttpRequest


class ILoginService(ABC):
    @abstractmethod
    def login(self, request: HttpRequest):
        pass


class LoginService(ILoginService):
    def __init__(self) -> None:
        pass

    def login(self, request: HttpRequest):
        pass

    def test(self) -> str:
        return "test success"
