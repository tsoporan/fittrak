from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from fittrak.utils.models import WorkoutBaseModel, UserBaseModel, BaseModel

import hashids

class Workout(BaseModel, UserBaseModel, WorkoutBaseModel):
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"

    STATUS_CHOICES = (
        (IN_PROGRESS, "In Progress"),
        (CANCELLED, "Cancelled"),
        (COMPLETE, "Complete"),
    )

    slug = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text='A human easy to read/share name for workout'
    )

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=IN_PROGRESS)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        format_by= "%Y-%m-%d %H:%m"
        start = self.date_started.strftime(format_by)
        end = "N/A"
        if self.date_ended:
            end = self.date_ended.strftime(format_by)

        return "{} -- {} to {}".format(self.user, start, end)


class ExerciseType(BaseModel, UserBaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Exercise(BaseModel, UserBaseModel, WorkoutBaseModel):
    workout = models.ForeignKey(
        Workout,
        null=True,
        related_name="exercises",
        blank=True,
        on_delete=models.CASCADE
    )

    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

    slug = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text='A human easy to read/share name for exercise'
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.exercise_type.name




class Set(BaseModel, WorkoutBaseModel):
    LB = "LB"
    KG = "KG"

    UNITS = [
        (KG, 'Kilograms'),
        (LB, 'Pounds'),
    ]

    exercise = models.ForeignKey(
        Exercise,
        related_name="sets",
        on_delete=models.CASCADE
    )
    repetitions = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    unit = models.CharField(max_length=32, choices=UNITS, default=LB)

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
