# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from days.models import Day
from sixweeks.helpers import render as six_weeks_render
from sixweeks.models import User

# Create your views here.

@login_required
def main(request):
    today = date.today()
    today_string = today.strftime('%Y-%m-%d')
    
    return redirect('day', cur_day=today_string)
    
@login_required
def staff_main(request):
    user = request.user
    params = {}

    cur_day = date.today()
    date_params = generateDayParams(cur_day)
    params.update(date_params)
    
    if user.is_staff:
        all_users = User.objects.all()
        params['users'] = all_users
        return six_weeks_render(request, 'staff_main.html', params)
    else:
        return redirect('main')


@login_required
def staff_user_report(request, user_id, cur_date):
    user = request.user
    params = {}

    cur_day = datetime.strptime(cur_date, '%Y-%m-%d').date()
    date_params = generateDayParams(cur_day)
    params.update(date_params)
    
    if user.is_staff:
        all_users = User.objects.all()
        params['users'] = all_users

        cur_user = None
        try:
            cur_user = User.objects.get(pk=user_id)
            params['selected_user'] = cur_user
        except User.DoesNotExist:
            pass
        
        day = None
        try:
            day = Day.objects.get(user=cur_user, date=cur_day)
            params['day'] = day
        except Day.DoesNotExist:        
            pass
        
        return six_weeks_render(request, 'staff_user_report.html', params)
    else:
        return redirect('main')

def generateDayParams(cur_day):
    time_delta_one_day = timedelta(days = 1)
    prev_day = cur_day - time_delta_one_day
    next_day = cur_day + time_delta_one_day

    params = {}
    params['cur_day'] = cur_day
    params['prev_day'] = prev_day
    params['next_day'] = next_day

    return params
