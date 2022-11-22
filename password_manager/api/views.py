from django.forms import model_to_dict
from generator.models import Password, User
from rest_framework.response import Response
from rest_framework.views import APIView

from generator.utils import generate_password


class CreatePasswordAPI(APIView):

    def post(self, request, token, key):
        user = User.objects.get(auth_token=token)
        password = Password.objects.create(
            key=key,
            link='link',
            description='description',
            password=generate_password(),
            user=user
        )

        return Response({'password': model_to_dict(password)})


class PasswordsAPI(APIView):

    def get(self, request, token):
        user = User.objects.get(auth_token=token)
        passwords = user.passwords.all().values()

        return Response({'passwords': list(passwords)})


class PasswordDetailAPI(APIView):

    def get(self, request, token, key):

        user = User.objects.get(auth_token=token)
        password = user.passwords.get(key=key)

        return Response({'password': model_to_dict(password)})
