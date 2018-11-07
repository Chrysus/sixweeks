# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django import forms

from points.models import Point

class CreatePointForm(forms.Form):
    title = forms.CharField(max_length=254, label="Title", required=True)
    description = forms.CharField(max_length=254, label="Description")
    point_value = forms.IntegerField(min_value=0, max_value=10, initial=1, required=True)

class CreatePointModelForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['title', 'description', 'point_value']
        widgets = {
            'description' : forms.Textarea(attrs={'cols' : 40, 'rows' : 6}),
        }
