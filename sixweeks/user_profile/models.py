# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models

from core.models import TimeStampedModel

class UserProfile(TimeStampedModel):
    weight = IntegerField()
    arm_left = IntegerField()
    arm_right = IntegerField()
    chest = IntegerField()
    waist = IntegerField()
    hips = IntegerField()
    thigh_left = IntegerField()
    thigh_right = IntegerField()

