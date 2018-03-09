from django.contrib import admin

from user_operation.models import UserFav, UserLeavingMsg, UserAddress


@admin.register(UserFav)
class UserFavAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLeavingMsg)
class UserLeavingMsgAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    pass
