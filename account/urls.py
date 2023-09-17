from django.urls import path

from account.views import Register, Test

urlpatterns = [
    path("/test", Test.as_view(), name="account.test"),
    path("/register", Register.as_view(), name="account.register"),
]