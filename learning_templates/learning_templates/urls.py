"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path

from basic_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('admin/', admin.site.urls),
    url(r'^basic_app/', include('basic_app.urls')),
    # url(r'^other/', views.other, name='other'),
    # url(r'^base/', views.base, name='base'),
    # url(r'^relative/', views.relative, name='relative'),
    # url(r'^other/' include('basic_app.urls')),
    # url(r'^relative/', include('basic_app.urls')),
    # url(r'base/', include('basic_app.urls'))
]
