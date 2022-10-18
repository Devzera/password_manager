from django.contrib import admin

from .models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'key',
        'link',
        'password',
        'user'
    )
    list_display_links = ('pk', 'key')
    search_fields = ('key',)
    empty_value_display = '-пусто-'
