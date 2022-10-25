from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Password, User


def home(request):
    template = 'storage/home.html'
    return render(request, template)


@login_required
def passwords(request, username):

    if username != request.user.username:
        return HttpResponse('<h1>Нет доступа</h1>')

    template = 'storage/profile.html'

    user = get_object_or_404(User, username=username)
    password = Password.objects.filter(user=user)

    context = {
        'passwords': password
    }

    return render(request, template, context)
