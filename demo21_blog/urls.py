"""demo21_blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from demo21_blog.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #富文本编辑器允许上传图片，会根据url路径
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^',include('postApp.urls')),
    #搜索插件已经配好了路由
    url(r'^search/',include('haystack.urls'))
]

from django.views.static import serve
if DEBUG:
    urlpatterns+=url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),