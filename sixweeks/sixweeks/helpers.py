# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.shortcuts import render as django_render
from django.template.loader import get_template as django_get_template

from datetime import date, timedelta

def render(request, template_name, context=None, status=None):
    if context == None:
        context = {}
        
    if 'cur_day' not in context:
        cur_day = date.today()
        time_delta_one_day = timedelta(days = 1)
        prev_day = cur_day - time_delta_one_day
        next_day = cur_day + time_delta_one_day

        context['cur_day'] = cur_day
        context['prev_day'] = prev_day
        context['next_day'] = next_day
    
    is_mobile_client = ((request.iOS == True) or (request.Android == True))
    if is_mobile_client:
        templates = ['mobile/' + template_name, template_name]
        return django_render(request, templates, context, status)

    return django_render(request, template_name, context, status)


def get_template(request, template_name):
    user = request.user
    template = template_name
    
    if user.is_staff:
        template = "staff_" + template_name

    return django_get_template(template)
