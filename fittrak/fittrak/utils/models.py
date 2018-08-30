from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserBaseModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WorkoutBaseModel(models.Model):
    date_started = models.DateTimeField(null=True, blank=True)
    date_ended = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def is_finished(self):
        return True if self.date_ended else False

    def delete(self):
        """ Overriden delete method to mark as inactive """
        self.is_active = False
        self.save()
