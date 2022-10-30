from django.forms import model_to_dict
from generator.models import Password, User
from rest_framework.response import Response
from rest_framework.views import APIView


class PasswordsAPI(APIView):

    def get(self, request):
        user = request.user
        print(user)
        passwords = user.passwords.all().values()

        return Response({'passwords': list(passwords)})


class PasswordDetailAPI(APIView):

    def get(self, request, key):

        user = request.user
        password = user.passwords.get(key=key)

        return Response({'passwords': model_to_dict(password)})
