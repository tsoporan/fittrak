from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from fittrack.utils.models import WorkoutBaseModel, UserBaseModel, BaseModel

import hashids

class WorkoutStatus(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Workout(BaseModel, UserBaseModel, WorkoutBaseModel):
    slug = models.CharField(max_length=15, unique=True, null=True, blank=True, help_text='A human easy to read/share name for workout')
    status = models.ForeignKey(WorkoutStatus, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.slug

class ExerciseType(BaseModel, UserBaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Exercise(BaseModel, WorkoutBaseModel):
    workout = models.ForeignKey(Workout, null=True, related_name="exercises", blank=True,
            on_delete=models.CASCADE)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    slug = models.CharField(max_length=15, unique=True, null=True, blank=True, help_text='A human easy to read/share name for exercise')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.type.name


MASS_UNITS = [
    ('KG', 'Kilograms'),
    ('LB', 'Pounds'),
]

class Set(BaseModel, WorkoutBaseModel):
    exercise = models.ForeignKey(Exercise, related_name="sets", on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    unit = models.CharField(max_length=32, choices=MASS_UNITS)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.id)


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
