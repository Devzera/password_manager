from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from generator.models import Password


class PasswordsAPI(APIView):

    def get(self, request, username):
        if request.user.username != username:
            return Response({'passwords': 'not allowed'})

        passwords = Password.objects.filter(user=request.user).values()

        return Response({'passwords': list(passwords)})


class PasswordDetailAPI(APIView):

    def get(self, request, username, key):
        if request.user.username != username:
            return Response({'passwords': 'not allowed'})

        password = Password.objects.get(key=key)

        return Response({'passwords': model_to_dict(password)})