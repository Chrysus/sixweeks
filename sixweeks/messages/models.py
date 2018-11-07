# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from __future__ import unicode_literals

from django.db import models

from core.models import TimeStampedModel

class Message(TimeStampedModel):
    from_user = ForeignKey('User')
    to_user = ForeignKey('User')
    message = TextField()
