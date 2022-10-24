from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from storage.models import User
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')


@login_required
def profile(request, username):
    if request.user.username != username:
        return HttpResponse('<h1>Нет доступа</h1>')

    template = 'users/profile.html'

    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, template, context)
