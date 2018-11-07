# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            error_message = 'Must provide a valid email address'
            raise ValueError(error_message)
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            error_message = 'Superuser must have is_staff set to true'
            raise ValueError(error_message)

        if extra_fields.get('is_superuser') is not True:
            error_message = 'Superuser must have is_superuser set to true'
            raise ValueError(error_message)
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    # remove the username from the base class and
    # force the email field to be unique
    
    username = None  
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
