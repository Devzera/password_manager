import random
from string import ascii_letters, digits, punctuation

from django.shortcuts import render


def generate_password(request):
    return render(
        request,
        template_name='generator/generate_password.html'
    )


def check_password(request):

    length = int(request.GET.get('length', 10))
    numbers = request.GET.get('numbers') == 'on'
    special = request.GET.get('special') == 'on'
    characters = ascii_letters

    if numbers:
        characters += digits
    if special:
        characters += punctuation

    password = ''
    for i in range(length):
        password += random.choice(characters)

    context = {
        'password': password
    }

    return render(
        request,
        template_name='generator/check_password.html',
        context=context
    )
