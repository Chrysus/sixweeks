# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from sixweeks.helpers import render as six_weeks_render

# Create your views here.

def mockSignInSignUp(request):
    signInSignUp_template = get_template('sign-in-sign-up.html')

    if signInSignUp_template is None:
        signInSignUp_template = "Hello World"

    return render(request, 'sign-in-sign-up.html')

def mockSignIn(request):
    signIn_template = get_template('sign-in.html')

    if signIn_template is None:
        signIn_template = "Hello World"

    return render(request, 'sign-in.html')

def mockSignUp(request):
    signUp_template = get_template('sign-up.html')

    if signUp_template is None:
        signUp_template = "Hello World"

    return render(request, 'sign-up.html')

def mockPoints(request):
    points_template = get_template('points.html')

    if points_template is None:
        points_template = "Hello World"

    return render(request, 'points.html')

def mockFitness(request):
    fitness_template = get_template('fitness.html')

    if fitness_template is None:
        fitness_template = "Hello World"

    return render(request, 'fitness.html')

def mockNutrition(request):
    nutrition_template = get_template('nutrition.html')

    if nutrition_template is None:
        nutrition_template = "Hello World"

    return render(request, 'nutrition.html')

def mockMessages(request):
    messages_template = get_template('messages.html')

    if messages_template is None:
        messsages_template = "Hello World"

    return render(request, 'messages.html')

def mockIndex(request):
#    index_template = get_template('index.html')
#
#    if index_template is None:
#        index_template = "Hello World"
#
    params = {}
    return six_weeks_render(request, 'index.html', params)

def mockMain(request):
    params = {}
    return six_weeks_render(request, 'main.html', params)
