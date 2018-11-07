# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

import string

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from sixweeks.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='First Name', label_suffix='')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Last Name', label_suffix='')
    email = forms.EmailField(max_length=254, required=True, help_text='Required.', label='Email Address', label_suffix='')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = string.capwords(self.fields['password1'].label)
        self.fields['password1'].label_suffix = ""
        self.fields['password2'].label = string.capwords(self.fields['password2'].label)
        self.fields['password2'].label_suffix = ""
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, label="Email")
    password = forms.CharField(max_length=254, label="Password", widget=forms.PasswordInput)
    
