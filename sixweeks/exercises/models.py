# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models

from django_extensions.db.models import TimeStampedModel

class Exercise(TimeStampedModel):
    # Enum
    OTHER = 0
    CARDIO = 1
    STRENGTH = 2

    EXERCISE_TYPE = (
        (OTHER, 'Other'),
        (CARDIO, 'Cardio'),
        (STRENGTH, 'Strength')
    )
    
    exercise_type = models.SmallIntegerField(choices=EXERCISE_TYPE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1023)
