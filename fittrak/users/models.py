from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model that inherits from the default Django user 
    - no special behaviour
    """
    pass


NOT_SET = "NOT_SET"
VERIFIED = "VERIFIED"

class Profile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verification_token = models.CharField(max_length=32, default=NOT_SET)

    class Meta:
        ordering = ('-id',)
