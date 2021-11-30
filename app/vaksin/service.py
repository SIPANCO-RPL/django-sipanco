from abc import ABC, abstractmethod
from django.http.request import HttpRequest
from injector import inject


# class ILoginService(ABC):
#     @abstractmethod
#     def login(self, request: HttpRequest):
#         raise NotImplementedError

#     def test(self) -> str:
#         return "test success"


# class LoginService(ILoginService):
#     @inject
#     def __init__(self) -> None:
#         pass

#     def login(self, request: HttpRequest):
#         a = request.method
#         pass

#     def test(self) -> str:
#         return "test success"


# class A:
#     @inject
#     def __init__(self, login_service: ILoginService):
#         self.login_service = login_service

#     def test(self):
#         return self.login_service.test()


'''

Controller -> Service -> Accessor/Repository

'''
