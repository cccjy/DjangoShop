"""DjangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views import View
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from DjangoShop import settings
from goods.views import GoodsViewSet, CategoryViewSet

router = DefaultRouter()
# register ViewSet
router.register('goods', GoodsViewSet, base_name='goods')
router.register('category', CategoryViewSet, base_name='category')

urlpatterns = [
    # 静态页面渲染
    path('home/', TemplateView.as_view(template_name='index.html'), name='index'),

    # admin
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),

    # django-restframework
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('docs/', include_docs_urls(title='DjangoShop')),
]

if settings.DEBUG:
    urlpatterns.append(
        re_path(r'^media/(?P<path>.*?)/$', serve, {'document_root': settings.MEDIA_ROOT})
    )
