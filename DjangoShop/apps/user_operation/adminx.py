import xadmin
from user_operation.models import UserFav
from user_operation.models import UserLeavingMsg
from user_operation.models import UserAddress


class UserFavAdmin(object):
    pass


class UserLeavingMsgAdmin(object):
    pass


class UserAddressAdmin(object):
    pass


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserLeavingMsg, UserLeavingMsgAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
