# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template

from points.models import Point
from sixweeks.helpers import render as six_weeks_render

from .forms import ExercisesForm, MealsForm
from .helpers import get_or_create
from .models import Day

# Create your views here.

# MAIN VIEW
@login_required
def index(request):
    return render(request, 'index.html')    

@login_required
def points(request, cur_day):
    params = {}

    points = Point.objects.all()
    params['points'] = points

    cur_date = datetime.strptime(cur_day, '%Y-%m-%d').date()
    date_params = generateDayParams(cur_date)
    params.update(date_params)
    
    user = request.user
    day = get_or_create(user=user, day=cur_day)
    if day:
        params['day'] = day

    if request.method == 'GET':
        pass

    need_to_save = False
    if request.method == 'POST':
        points_checked = request.POST.getlist("points")
        day.points.clear()
        for point_id in points_checked:
            found_point = None
            try:
                found_point = Point.objects.get(pk=point_id)
            except:
                pass
            
            if found_point:
                if not day.points.filter(pk=found_point.pk).exists():
                    day.points.add(found_point)

            day.save()

    if day:
        checked_points = []
        for point in day.points.all():
            checked_points.append(point.pk)
        params['checked_points'] = checked_points

    return six_weeks_render(request, 'points.html', params)

@login_required
def fitness(request, cur_day):
    params = {}

    cur_date = datetime.strptime(cur_day, '%Y-%m-%d').date()
    date_params = generateDayParams(cur_date)
    params.update(date_params)

    user = request.user
    day = get_or_create(user=user, day=cur_day)
    if day:
        params['day'] = day

    if request.method == 'GET':
        form_data = {}
        form_data['cardio'] = day.cardio.description
        form_data['strength'] = day.strength.description

        form = ExercisesForm(data=form_data)

        params['form'] = form

    if request.method == 'POST':
        form = ExercisesForm(request.POST)
        if form.is_valid():
            cardio = form.cleaned_data.get('cardio')
            strength = form.cleaned_data.get('strength')

            day.cardio.description = cardio
            day.strength.description = strength

            day.cardio.save()
            day.strength.save()
            day.save()

            params['form'] = form

        else:
            error_message = "Error: " + form.errors.as_json()
            context = {'form' : form, 'error_message' : error_message}
            params.update(context)
            return six_weeks_render(request, 'fitness.html', params)

    return six_weeks_render(request, 'fitness.html', params)

@login_required
def nutrition(request, cur_day):
    params = {}

    cur_date = datetime.strptime(cur_day, '%Y-%m-%d').date()
    date_params = generateDayParams(cur_date)
    params.update(date_params)
    
    user = request.user
    day = get_or_create(user=user, day=cur_day)
    if day:
        params['day'] = day

    if request.method == 'GET':
        form_data = {}
        form_data['breakfast'] = day.breakfast.description
        form_data['lunch'] = day.lunch.description
        form_data['dinner'] = day.dinner.description
        form_data['snacks'] = day.snacks.description

        form = MealsForm(data=form_data)

        params['form'] = form

    if request.method == 'POST':
        form = MealsForm(request.POST)
        if form.is_valid():
            breakfast = form.cleaned_data.get('breakfast')
            lunch = form.cleaned_data.get('lunch')
            dinner = form.cleaned_data.get('dinner')
            snacks = form.cleaned_data.get('snacks')

            day.breakfast.description = breakfast
            day.lunch.description = lunch
            day.dinner.description = dinner
            day.snacks.description = snacks

            day.breakfast.save()
            day.lunch.save()
            day.dinner.save()
            day.snacks.save()
            day.save()

            params['form'] = form

        else:
            error_message = "Error: " + form.errors.as_json()
            context = {'form' : form, 'error_message' : error_message}
            params.update(context)
            return six_weeks_render(request, 'nutrition.html', params)


    return six_weeks_render(request, 'nutrition.html', params)

@login_required
def messages(request, cur_day):
    params = {}

    cur_date = datetime.strptime(cur_day, '%Y-%m-%d').date()

    user = request.user
    day = get_or_create(user=user, day=cur_day)
    if day:
        params['day'] = day

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return six_weeks_render(request, 'messages.html', params)

@login_required
def day(request, cur_day):
    params = {}

    path = request.build_absolute_uri()
    date_string = path.rsplit('/', 1)[-1]
    
    cur_day = datetime.strptime(date_string, '%Y-%m-%d').date()
    time_delta_one_day = timedelta(days = 1)
    prev_day = cur_day - time_delta_one_day
    next_day = cur_day + time_delta_one_day

    params['cur_day'] = cur_day
    params['prev_day'] = prev_day
    params['next_day'] = next_day

    user = request.user
    day = get_or_create(user=user, day=cur_day)
    if day:
        params['day'] = day

    return six_weeks_render(request, 'main.html', params)


def generateDayParams(cur_day):
    time_delta_one_day = timedelta(days = 1)
    prev_day = cur_day - time_delta_one_day
    next_day = cur_day + time_delta_one_day

    params = {}
    params['cur_day'] = cur_day
    params['prev_day'] = prev_day
    params['next_day'] = next_day

    return params
