from django.contrib import admin

from users.models import UserProfile, VerifyCode

admin.site.site_header = '商城后台管理'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'name', 'gender', 'mobile']


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile']
