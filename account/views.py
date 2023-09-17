from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from account.serializers import UserSerializer
from account.models import UserData


class Register(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.filter()


class Test(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.filter()
    permission_classes = [IsAuthenticated]