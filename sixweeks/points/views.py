# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from points.forms import CreatePointForm, CreatePointModelForm
from points.models import CreatePoint, Point
from sixweeks.helpers import render as six_weeks_render
from sixweeks.models import User

# Create your views here.

@login_required
def points(request):
    params = {}

    points = Point.objects.all()
    params['points'] = points
    
    return six_weeks_render(request, 'points.html', params)

@staff_member_required
def pointsAdmin(request):
    user = request.user
    params = {}

    cur_day = date.today()
    date_params = generateDayParams(cur_day)
    params.update(date_params)
    
    if request.method == 'POST':
        form = CreatePointModelForm(request.POST)
        if form.is_valid():
            form.save()
            
    all_users = User.objects.all()
    params['users'] = all_users

    all_points = Point.objects.all()
    params['points'] = all_points
    
    form = CreatePointForm()
    params['form'] = form

    return render(request, 'staff_points.html', params)

def generateDayParams(cur_day):
    time_delta_one_day = timedelta(days = 1)
    prev_day = cur_day - time_delta_one_day
    next_day = cur_day + time_delta_one_day

    params = {}
    params['cur_day'] = cur_day
    params['prev_day'] = prev_day
    params['next_day'] = next_day

    return params
