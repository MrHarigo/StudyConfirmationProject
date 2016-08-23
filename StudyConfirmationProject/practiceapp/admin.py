from django.contrib import admin
from .models import Certificate, Request
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MySiteProfile


class UserInline(admin.StackedInline):
    model = MySiteProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Certificate)
admin.site.register(Request)