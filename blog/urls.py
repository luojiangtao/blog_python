"""blog URL Configuration

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
from django.urls import path
from django.conf.urls import url

from .controller.index import index
from .controller.index import article
from .controller.admin import login

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    url(r'^admin/login$', login.index,name='login'),

    url(r'^$', index.index,name='index'),
    url(r'^detail$', article.detail,name='detail'),
    url(r'^list$', article.list,name='list'),
]
