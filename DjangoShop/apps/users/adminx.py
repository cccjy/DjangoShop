import xadmin
from xadmin import views
from users.models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'DjangoShop'
    site_footer = 'DjangoShop'
    menu_style = 'accordion'


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
