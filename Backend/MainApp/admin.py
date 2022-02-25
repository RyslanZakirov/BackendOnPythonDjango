from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import OwnUser, Guest, Point, Tag, Photo, PointMessage, UserMessage

class CustomerOwnUser(UserAdmin):

    list_display = ('userId', 'login', 'userCity', 'rating', 'hasUserActivePoint')
    list_display_links = ('login',)
    list_filter = ('userCity', 'rating', 'hasUserActivePoint', 'is_superuser')

    ordering = ('userId', 'userCity', 'rating', 'hasUserActivePoint')
    search_fields = ('login', 'userCity')

    fieldsets = (
        ('Общие данные', {'fields': ('login', 'userCity', 'phone', 'rating', 'hasUserActivePoint', 'userImage')}),
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


class CustomerPoint(admin.ModelAdmin):

    list_display = ('pointId', 'name', 'city', 'street', 'houseNumber', 'rating')
    list_display_links = ('pointId',)
    list_filter = ('name', 'city', 'rating', 'timeCreation', 'isVisible')

    ordering = ('pointId', 'rating')
    search_fields = ('name', 'city')

    # fieldsets = (
    #     ('Общая информация', {'fields': ('pointId', 'name', 'description', 'rating', 'isVisible')}),
    #     ('Время', {'fields': ('timeCreation', 'timeDuration')}),
    #     ('Расположение', {'fields': ('city', 'street', 'houseNumber', 'latitude', 'longitude')}),
    #     ('Справочная информация', {'fields': ('instagram', 'vk', 'telegram')})
    # )

admin.site.register(Point, CustomerPoint)


class CustomerGuest(admin.ModelAdmin):

    list_display = ('guestId', 'pointId', 'userId')
    list_display_links = ('guestId',)

admin.site.register(Guest, CustomerGuest)


class CustomerTag(admin.ModelAdmin):

    list_display = ('tagId', 'tagName', 'pointId')
    list_display_links = ('tagId',)
    list_filter = ('tagName',)

    search_fields = ('tagName',)

admin.site.register(Tag, CustomerTag)


class CustomerPhoto(admin.ModelAdmin):

    list_display = ('photoId', 'pointId')
    list_display_links = ('pointId',)

admin.site.register(Photo, CustomerPhoto)


class CustomerPointMessage(admin.ModelAdmin):

    list_display = ('pointMessageId', 'userId', 'pointId', 'pointMessageDate')
    list_display_links = ('pointMessageId',)

    ordering = ('pointMessageDate',)

admin.site.register(PointMessage, CustomerPointMessage)


class CustomerUserMessage(admin.ModelAdmin):

    list_display = ('userMessageId', 'senderId', 'receiverId', 'userMessageDate')
    list_display_links = ('userMessageId',)

    ordering = ('userMessageDate',)

admin.site.register(UserMessage, CustomerUserMessage)