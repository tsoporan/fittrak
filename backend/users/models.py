from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
