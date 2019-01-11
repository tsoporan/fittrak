from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

NOT_SET = "NOT_SET"
VERIFIED = "VERIFIED"


class User(AbstractUser):
    """
    Custom user model that inherits from the default Django user
    - no special behaviour
    """

    pass


class Profile(models.Model):
    LBS = "LBS"
    KGS = "KGS"

    PREFERRED_UNITS = ((LBS, "LBS"), (KGS, "KGS"))

    date_created = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verification_token = models.CharField(max_length=32, default=NOT_SET)

    height = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    weight = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    preferred_unit = models.CharField(
        choices=PREFERRED_UNITS, max_length=3, default=LBS
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.user}"
