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
def fitness(request):
    fitness_template = get_template('fitness.html')

    if fitness_template is None:
        fitness_template = "Hello World"

    return six_weeks_render(request, 'fitness.html')
