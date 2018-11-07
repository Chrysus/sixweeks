# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^(?P<cur_day>\d{4}-\d{2}-\d{2})/points', views.points, name='day_points'),
    url(r'^(?P<cur_day>\d{4}-\d{2}-\d{2})/fitness', views.fitness, name='day_fitness'),
    url(r'^(?P<cur_day>\d{4}-\d{2}-\d{2})/nutrition', views.nutrition, name='day_nutrition'),
    url(r'^(?P<cur_day>\d{4}-\d{2}-\d{2})/messages', views.messages, name='day_messages'),
    url(r'^(?P<cur_day>\d{4}-\d{2}-\d{2})', views.day, name='day'),
    url(r'^$', views.index, name='index'),
]
