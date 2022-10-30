from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Password(models.Model):
    key = models.SlugField(
        'ключ',
        unique=True,
        null=True
    )
    link = models.TextField(
        'ссылка',
        null=True,
        blank=True
    )
    description = models.TextField(
        'описание',
        max_length=300,
        null=True,
        blank=True
    )
    password = models.CharField(
        'пароль',
        max_length=32
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name='passwords'
    )

    class Meta:
        verbose_name = 'пароль'
        verbose_name_plural = 'пароли'

    def __str__(self):
        return self.key

    def get_absolute_url(self):
        return reverse('passwords:password_detail', kwargs={'key': self.key})
