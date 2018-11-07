# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import get_template

from accounts.forms import SignUpForm, SignInForm
from sixweeks.helpers import render

# Create your views here.

def SignInSignUp(request):
    return render(request, 'sign-in-sign-up.html')

def SignIn(request):
    if request.method == 'GET':
        form = SignInForm()
        return render(request, 'sign-in.html', {'form' : form})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_staff:
                        return redirect('staff_main')
                    else:
                        return redirect('main')

    return HttpResponseRedirect('#dlg-invalid-credentials')


def SignUp(request):

    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'sign-up.html', {'form' : form})

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/sixweeks/index')
        else:
            error_message = "Error: " + form.errors.as_json()
            context = {'form' : form, 'error_message' : error_message}
            return render(request, 'sign-up.html', context)

    return render(request, 'sign-up.html')

def SignOut(request):
    logout(request)

    return redirect('/sixweeks/accounts/sign-in.html')
