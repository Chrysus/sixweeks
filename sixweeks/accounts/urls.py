# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sign-in-sign-up', views.SignInSignUp, name='sign-in-sign-up'),
    url(r'^sign-in', views.SignIn, name='sign-in'),
    url(r'^sign-up', views.SignUp, name='sign-up'),
    url(r'^sign-out', views.SignOut, name='sign-out'),
    url(r'^$', views.SignInSignUp, name='sign-in-sign-up'),
]
