# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django import forms

class MealsForm(forms.Form):
    textarea_attrs = {'rows' : 8, 'cols' : 40, 'class' : 'form-control'}
    breakfast = forms.CharField(max_length=254, label="Breakfast", widget=forms.Textarea(attrs=textarea_attrs), required=False)
    lunch = forms.CharField(max_length=254, label="Lunch", widget=forms.Textarea(attrs=textarea_attrs), required=False)
    dinner = forms.CharField(max_length=254, label="Dinner", widget=forms.Textarea(attrs=textarea_attrs), required=False)
    snacks = forms.CharField(max_length=254, label="Snacks", widget=forms.Textarea(attrs=textarea_attrs), required=False)

class ExercisesForm(forms.Form):
    textarea_attrs = {'rows' : 8, 'cols' : 40, 'class' : 'form-control'}
    cardio = forms.CharField(max_length=254, label="Cardio", widget=forms.Textarea(attrs=textarea_attrs), required=False)
    strength = forms.CharField(max_length=254, label="Strength", widget=forms.Textarea(attrs=textarea_attrs), required=False)
