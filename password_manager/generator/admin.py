from django.contrib import admin

from generator.models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'key',
        'link',
        'password',
        'updated_at',
        'created_at',
        'user'
    )
    list_display_links = ('pk', 'key')
    search_fields = ('key',)
    empty_value_display = '-пусто-'
