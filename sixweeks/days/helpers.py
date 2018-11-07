# -*- coding: utf-8 -*-
#
# Copyright 2017 Chrysus
# Licensed under MIT (https://github.com/Chrysus/sixweeks/blob/master/LICENSE)

from .models import Day
from exercises.models import Exercise
from meals.models import Meal

def get_or_create(user, day):
    try:
        day = Day.objects.get(user=user, date=day)
        return day
    except Day.DoesNotExist:        
        breakfast = Meal(meal_type=Meal.BREAKFAST)
        lunch = Meal(meal_type=Meal.LUNCH)
        dinner = Meal(meal_type=Meal.DINNER)
        snacks = Meal(meal_type=Meal.SNACK)

        cardio = Exercise(exercise_type=Exercise.CARDIO)
        strength = Exercise(exercise_type=Exercise.STRENGTH)
        extra_activity = Exercise(exercise_type=Exercise.OTHER)

        breakfast.save()
        lunch.save()
        dinner.save()
        snacks.save()
        
        cardio.save()
        strength.save()
        extra_activity.save()
        
        new_day = Day(user=user, date=day, breakfast=breakfast, lunch=lunch, dinner=dinner, snacks=snacks, cardio=cardio, strength=strength, extra_activity=extra_activity)

        new_day.save()
        
        return new_day

    return NULL
