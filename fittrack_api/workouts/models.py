from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel, UserBaseModel

# Create your models here.
class Workout(UserBaseModel):
    pass

class Exercise(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True)
    workout = models.ForeignKey(Workout)

class Set(UserBaseModel):
    exercise = models.ForeignKey(Exercise)
    repetitions = models.PositiveIntegerField()
