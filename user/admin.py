from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'joined_at', 'last_login_at', 'is_superuser', 'is_active')
    list_display_links = ('id', 'email')

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")
    
    def last_login_at(self, obj):
        if not obj.last_login:
            return ""
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    joined_at.admin_order_field = "-date_joined"
    joined_at.short_descripion = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_descripion = '최근로그인'
