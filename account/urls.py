from django.urls import path

from account.views import Login, Register, Test

urlpatterns = [
    path("/login", Login.as_view(), name="account.login"),
    path("/register", Register.as_view(), name="account.register"),
    path("/test", Test.as_view(), name="account.test"),
]