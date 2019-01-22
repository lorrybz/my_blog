"""DjangoExtSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static

from DjangoExtSystem import settings
from utils.upload_image import upload_image

from front import views
urlpatterns = [
    path(r'app/', include(('app.urls', 'app'), namespace='app')),
    path('', views.index),
    path(r'users/', include(('users.urls', 'users'), namespace='users')),
    path(r'front/', include(('front.urls', 'front'), namespace='front')),
    # kindeditor编辑器上传图片地址
    re_path(r'^util/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]

# 配置media访问路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

