from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import OwnUser

class CustomerOwnUser(UserAdmin):

    list_display = ('userId', 'login', 'userCity', 'rating', 'hasUserActivePoint')
    list_display_links = ('login',)
    list_filter = ('userCity', 'rating', 'hasUserActivePoint', 'is_superuser')

    ordering = ('userId', 'userCity', 'rating', 'hasUserActivePoint')
    search_fields = ('login', 'userCity')

    fieldsets = (
        ('Общие данные', {'fields': ('login', 'userCity', 'rating', 'hasUserActivePoint')}),
        ('Статус пользователя', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Полномочия', {'fields': ('groups', 'user_permissions')})
    )

    add_fieldsets = (
        ('Создание нового пользователя', {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2')
        }),
    )

admin.site.register(OwnUser, CustomerOwnUser)
