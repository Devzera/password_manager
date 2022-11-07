from generator.models import Password
from rest_framework import serializers


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ('key', 'password', 'user')
