from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, View
from generator.models import User

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['username'])


class ProfileChangeInfoView(LoginRequiredMixin, View):

    def get(self, request, username):
        return render(
            request,
            'users/profile_edit.html',
            context={'user': User.objects.get(username=request.user.username)}
        )

    def post(self, request, username):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = User.objects.get(username=request.user.username)
        user.first_name = first_name or user.first_name
        user.last_name = last_name or user.last_name
        user.username = username or user.username
        user.email = email or user.email
        user.save()
        return redirect('accounts:profile', request.user.username)
