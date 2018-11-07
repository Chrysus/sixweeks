# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

"""sixweeks_project URL Configuration

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

from . import views
from mock.views import mockIndex

urlpatterns = [
    url(r'^mock/', include('mock.urls')),
    url(r'^accounts/', include('accounts.urls')),
    # These should probably be app-ified at some point
    url(r'^days/', include('days.urls')),
    url(r'^points/', include('points.urls')),
    url(r'^fitness/', include('exercises.urls')),
    url(r'^nutrition/', include('meals.urls')),
    url(r'^messages/', include('messages.urls')),
    url(r'^staff/(?P<user_id>\d+)/(?P<cur_date>\d{4}-\d{2}-\d{2})/', views.staff_user_report, name='staff_user_report'),
    url(r'^staff/', views.staff_main, name='staff_main'),
    url(r'^', views.main, name='main'),
    # end app-ify section
]

