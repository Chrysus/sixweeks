# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

class Meal(TimeStampedModel):
    # Enum
    OTHER = 0
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    SNACK = 4

    MEAL_TYPE = (
        (OTHER, 'Other'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACK, 'Snack')
    )
    
    meal_type = models.SmallIntegerField(choices=MEAL_TYPE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1023)
