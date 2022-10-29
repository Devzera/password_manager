from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, ListView, DetailView

from .utils import generate_password
from .models import Password, User


class HomeView(TemplateView):
    template_name = 'generator/home.html'


class CreatePasswordView(LoginRequiredMixin, TemplateView):
    template_name = 'generator/create_password.html'


class SavePasswordView(LoginRequiredMixin, View):

    def post(self, request):

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

        return redirect('passwords:password_detail', key)


class PasswordsView(LoginRequiredMixin, ListView):
    template_name = 'generator/passwords.html'
    context_object_name = 'passwords'

    def get_queryset(self):
        user = self.request.user
        return Password.objects.filter(user=user)


class PasswordDetailView(LoginRequiredMixin, DetailView):
    template_name = 'generator/password_detail.html'
    model = Password
    slug_url_kwarg = 'key'
    context_object_name = 'password'

    # def get_queryset(self):
    #     user = self.request.user
    #     password = get_object_or_404(Password, user=user)
    #     return password.objects.get(key=key)


@login_required
def password_detail(request, key):

    password = get_object_or_404(Password, key=key)

    if request.user != password.user:
        return redirect('passwords:passwords')

    context = {
        'password': password
    }

    return render(
        request,
        template_name='generator/password_detail.html',
        context=context
    )


@login_required
def change_password(request, key):
    password = get_object_or_404(Password, key=key)

    if password.user != request.user:
        return HttpResponse('<h1>Нет доступа</h1>')

    password.password = generate_password(24, True, True)
    password.save()

    return redirect('passwords:password_detail', key)
