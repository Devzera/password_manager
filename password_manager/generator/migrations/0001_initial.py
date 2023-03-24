# Generated by Django 3.2 on 2023-03-24 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(help_text='Ключ доступа для вашего пароля', null=True, verbose_name='ключ')),
                ('link', models.URLField(blank=True, help_text='Ссылка на ресурс, где используется пароль', null=True, verbose_name='ссылка')),
                ('description', models.TextField(blank=True, help_text='Описание', max_length=300, null=True, verbose_name='описание')),
                ('password', models.CharField(max_length=32, verbose_name='пароль')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, help_text='Когда последний раз обновляли пароль', verbose_name='дата обновления')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Когда был создан пароль', verbose_name='дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'пароль',
                'verbose_name_plural': 'пароли',
                'unique_together': {('user', 'key')},
            },
        ),
    ]
