from django.contrib import admin

from .models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'abbreviation',
        'link',
        'password',
        'user'
    )
    list_display_links = ('pk', 'abbreviation')
    search_fields = ('abbreviation',)
    empty_value_display = '-пусто-'
