from django.db import models
from django.contrib.auth.models import User

class UserBaseModel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        abstract = True

class WorkoutBaseModel(UserBaseModel):
    date_started = models.DateTimeField(null=True, blank=True)
    date_ended = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def delete(self):
        """ Overriden delete method to mark as inactive """
        self.is_active = False
        self.save()

