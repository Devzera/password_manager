import random
from string import ascii_letters, digits, punctuation

from django.shortcuts import render, redirect, get_object_or_404

from storage.models import Password


def create_password(request):
    return render(
        request,
        template_name='generator/create_password.html'
    )


def save_password(request):

    key = request.POST.get('key')
    link = request.POST.get('link')
    description = request.POST.get('description')
    length = int(request.POST.get('length', 10))
    user = request.user

    numbers = request.POST.get('numbers') == 'on'
    special = request.POST.get('special') == 'on'
    characters = ascii_letters

    if numbers:
        characters += digits
    if special:
        characters += punctuation

    password = ''
    for i in range(length):
        password += random.choice(characters)

    Password.objects.create(
        key=key,
        link=link,
        description=description,
        password=password,
        user=user
    )

    return redirect('generator:password_detail', key)


def password_detail(request, key):

    password = get_object_or_404(Password, key=key)
    context = {
        'password': password.password
    }

    return render(
        request,
        template_name='generator/password_detail.html',
        context=context
    )
