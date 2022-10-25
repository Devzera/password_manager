from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from generator.utils import generate_password
from storage.models import Password


@login_required
def create_password(request):
    return render(
        request,
        template_name='generator/create_password.html'
    )


@login_required
def save_password(request):

    key = request.POST.get('key')
    link = request.POST.get('link')
    description = request.POST.get('description')
    length = int(request.POST.get('length', 10))
    user = request.user

    numbers = request.POST.get('numbers') == 'on'
    special = request.POST.get('special') == 'on'

    password = generate_password(length, numbers, special)

    Password.objects.create(
        key=key,
        link=link,
        description=description,
        password=password,
        user=user
    )

    return redirect('generator:password_detail', (request.user.username, key))


@login_required
def change_password(request, username, key):
    password = get_object_or_404(Password, key=key)

    if password.user != request.user:
        return HttpResponse('<h1>Нет доступа</h1>')

    password.password = generate_password(24, True, True)
    password.save()

    return redirect('generator:password_detail', (request.user.username, key))


@login_required
def password_detail(request, username, key):

    if request.user.username != username:
        return HttpResponse('<h1>Нет доступа</h1>')

    password = get_object_or_404(Password, key=key)
    context = {
        'password': password
    }

    return render(
        request,
        template_name='generator/password_detail.html',
        context=context
    )

