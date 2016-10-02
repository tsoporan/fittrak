from django.db import models
from django.contrib.auth.models import User

from utils.models import WorkoutBaseModel

class Workout(WorkoutBaseModel):
    
    class Meta:
        ordering = ('-id',)

class Exercise(WorkoutBaseModel):
    workout = models.ForeignKey(Workout)
    name = models.CharField(max_length=250, unique=True, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

class Set(WorkoutBaseModel):
    exercise = models.ForeignKey(Exercise)

    repetitions = models.PositiveIntegerField()

    class Meta:
        ordering = ('-id',)
