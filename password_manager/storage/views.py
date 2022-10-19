from django.shortcuts import render, get_object_or_404

from .models import Password, User


def profile(request, username):
    template = 'storage/profile.html'

    user = get_object_or_404(User, username=username)
    password = Password.objects.filter(user=user)

    context = {
        'passwords': password
    }

    return render(request, template, context)
