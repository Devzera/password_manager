from rest_framework import serializers

from generator.models import Password


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ('key', 'password', 'user')
