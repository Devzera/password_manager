from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Password(models.Model):
    key = models.SlugField(
        'ключ',
        unique=True,
        null=True,
        help_text='Ключ доступа для вашего пароля'
    )
    link = models.URLField(
        'ссылка',
        null=True,
        blank=True,
        help_text='Ссылка на ресурс, где используется пароль'
    )
    description = models.TextField(
        'описание',
        max_length=300,
        null=True,
        blank=True,
        help_text='Описание'
    )
    password = models.CharField(
        'пароль',
        max_length=32
    )
    updated_at = models.DateTimeField(
        'дата обновления',
        db_index=True,
        auto_now=True,
        help_text='Когда последний раз обновляли пароль'
    )
    created_at = models.DateTimeField(
        'дата создания',
        db_index=True,
        auto_now_add=True,
        help_text='Когда был создан пароль'
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
