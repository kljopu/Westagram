from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'joined_at', 'last_login_at', 'is_superuser', 'is_activate')