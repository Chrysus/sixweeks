# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin', views.pointsAdmin, name='points_admin'),
    url(r'^', views.points, name='points'),
]
