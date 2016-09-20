from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel

# Create your models here
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

