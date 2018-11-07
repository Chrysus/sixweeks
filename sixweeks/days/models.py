# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models

class Day(models.Model):
    date = models.DateField()

    user = models.ForeignKey('sixweeks.User', unique_for_date='date', on_delete=models.CASCADE)

    breakfast = models.ForeignKey('meals.Meal', on_delete=models.PROTECT, related_name='+')
    lunch = models.ForeignKey('meals.Meal', on_delete=models.PROTECT, related_name='+')
    dinner = models.ForeignKey('meals.Meal', on_delete=models.PROTECT, related_name='+')
    snacks = models.ForeignKey('meals.Meal', on_delete=models.PROTECT, related_name='+')
    water_intake = models.IntegerField(blank=True, null=True)

    points = models.ManyToManyField('points.Point')

    cardio = models.ForeignKey('exercises.Exercise', on_delete=models.PROTECT, related_name='+')
    strength = models.ForeignKey('exercises.Exercise', on_delete=models.PROTECT, related_name='+')
    extra_activity = models.ForeignKey('exercises.Exercise', on_delete=models.PROTECT, related_name='+')

    class Meta:
        unique_together = ('date', 'user',)
