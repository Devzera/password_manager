from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Password(models.Model):
    key = models.SlugField(
        'Ключ',
        unique=True,
        null=True
    )
    link = models.TextField(
        'Ссылка',
        null=True,
        blank=True
    )
    description = models.TextField(
        'Описание',
        max_length=300,
        null=True,
        blank=True
    )
    password = models.CharField(
        'Пароль',
        max_length=32
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='passwords'
    )

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'

    def __str__(self):
        return self.key
