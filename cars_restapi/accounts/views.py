from django.contrib.auth import get_user_model
from rest_framework import generics as api_views

from cars_restapi.accounts.serializers import CreateUserSerializer

UserModel = get_user_model()


class RegisterView(api_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer

