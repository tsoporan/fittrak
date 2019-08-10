from django.conf import settings
from django.db import models


class UserBaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Overriden delete method to mark as inactive """
        self.is_active = False
        self.save()
