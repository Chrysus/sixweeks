# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from sixweeks.helpers import render as six_weeks_render

# Create your views here.

@login_required
def messages(request):
    messages_template = get_template('messages.html')

    if messages_template is None:
        messsages_template = "Hello World"

    return render(request, 'messages.html')
