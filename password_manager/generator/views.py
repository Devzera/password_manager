from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView, View

from .models import Password
from .utils import generate_password


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
        return Password.objects.filter(user=self.request.user)


class PasswordDetailView(LoginRequiredMixin, DetailView):
    model = Password
    template_name = 'generator/password_detail.html'
    slug_field = 'key'
    slug_url_kwarg = 'key'
    context_object_name = 'password'

    def get_queryset(self):
        return Password.objects.filter(
            user=self.request.user,
            key=self.kwargs['key']
        )


class ChangePasswordView(LoginRequiredMixin, View):

    def post(self, request, key):
        user = request.user
        password = get_object_or_404(Password, key=key, user=user)
        password.password = generate_password(24, True, True)
        password.save()
        return redirect('passwords:password_detail', key)
