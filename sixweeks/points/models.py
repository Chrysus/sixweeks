# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models

class Point(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    point_value = models.IntegerField()
    available = models.BooleanField(default=True)

def CreatePoint(title, description, point_value):
    new_point = Point()
    new_point.title = title
    new_point.description = description
    new_point.point_value = point_value
    new_point.available = True

    new_point.save()
