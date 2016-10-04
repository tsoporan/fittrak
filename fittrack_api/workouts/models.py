from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from django.contrib.auth.models import User

from utils.models import WorkoutBaseModel

import hashids

class Workout(WorkoutBaseModel):
    display_name = models.CharField(max_length=15, unique=True, null=True, blank=True, help_text='A human easy to read/share name for workout')

    class Meta:
        ordering = ('-id',)

    def delete(self):
        """ Overriden delete method to mark as inactive """
        self.is_active = False
        self.save()

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

@receiver(post_save, sender=Workout)
def set_display_name(sender, instance, **kwargs):
    if not instance.display_name:
        h = hashids.Hashids(salt=settings.HASHIDS_SALT)
        instance.display_name = h.encode(instance.id)
        instance.save()
