from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserBaseModel(BaseModel):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True
