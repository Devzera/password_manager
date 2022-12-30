from django import forms

from generator.models import Password


class CreatePasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('key', 'link')
