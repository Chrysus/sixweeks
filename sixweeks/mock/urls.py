# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sign-in-sign-up', views.mockSignInSignUp, name='sign-in-sign-up'),
    url(r'^sign-in', views.mockSignIn, name='sign-in'),
    url(r'^sign-up', views.mockSignUp, name='sign-up'),
    url(r'^index', views.mockIndex, name='index'),
    url(r'^points', views.mockPoints, name='points'),
#    url(r'^points', views.mockPoints, name='points'),
    url(r'^fitness', views.mockFitness, name='fitness'),
    url(r'^nutrition', views.mockNutrition, name='nutrition'),
    url(r'^messages', views.mockMessages, name='messages'),
    url(r'^main', views.mockMain, name='main'),
    url(r'^$', views.mockIndex, name='index'),
]
