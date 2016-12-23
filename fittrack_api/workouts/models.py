from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from django.contrib.auth.models import User

from utils.models import WorkoutBaseModel

import hashids

class Workout(WorkoutBaseModel):
    slug = models.CharField(max_length=15, unique=True, null=True, blank=True, help_text='A human easy to read/share name for workout')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.slug

class Exercise(WorkoutBaseModel):
    workout = models.ForeignKey(Workout, null=True, blank=True)
    name = models.CharField(max_length=250, unique=True, null=True, blank=True)
    slug = models.CharField(max_length=15, unique=True, null=True, blank=True, help_text='A human easy to read/share name for exercise')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


MASS_UNITS = [
    ('KG', 'Kilograms'),
    ('LB', 'Pounds'),
]

class Set(WorkoutBaseModel):
    exercise = models.ForeignKey(Exercise)
    repetitions = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    unit = models.CharField(max_length=32, choices=MASS_UNITS)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.exercise.name

@receiver(post_save, sender=Workout)
def set_workout_slug(sender, instance, **kwargs):
    if not instance.slug:
        h = hashids.Hashids(salt=settings.HASHIDS_SALT)
        instance.slug = h.encode(instance.id)
        instance.save()

@receiver(post_save, sender=Exercise)
def set_exercise_slug(sender, instance, **kwargs):
    if not instance.slug:
        h = hashids.Hashids(salt=settings.HASHIDS_SALT)
        instance.slug = h.encode(instance.id)
        instance.save()
