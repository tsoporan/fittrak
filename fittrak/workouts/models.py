import hashids
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from fittrak.utils.models import BaseModel, UserBaseModel, WorkoutBaseModel


class Workout(BaseModel, UserBaseModel, WorkoutBaseModel):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (CANCELLED, "Cancelled"),
        (COMPLETE, "Complete"),
    )

    slug = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="A human easy to read/share name for workout",
    )

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        format_by = "%Y-%m-%d %H:%m"
        start = self.date_started.strftime(format_by)
        end = "N/A"

        if self.date_ended:
            end = self.date_ended.strftime(format_by)

        return f"{self.user} - Start: {start} - End: {end}"


class WorkoutEvent(BaseModel, UserBaseModel):
    """
    Tracks state change on a Workout
    """

    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    action = models.CharField(max_length=64)
    message = models.TextField(
        blank=True, help_text="Store the human friendly representation of the change"
    )

    # DjangoJSONEncoder deals with datetimes and uuids, default encoder does not
    state = JSONField(encoder=DjangoJSONEncoder, help_text="Store the model state")

    def __str__(self):
        return f"{self.workout}"


class MuscleGroup(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class ExerciseType(BaseModel, UserBaseModel):
    name = models.CharField(max_length=250)
    muscle_group = models.ForeignKey(
        MuscleGroup, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return self.name


class Exercise(BaseModel, UserBaseModel, WorkoutBaseModel):
    workout = models.ForeignKey(
        Workout,
        null=True,
        related_name="exercises",
        blank=True,
        on_delete=models.CASCADE,
    )

    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

    slug = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="A human easy to read/share name for exercise",
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.exercise_type.name


class Set(BaseModel, UserBaseModel, WorkoutBaseModel):
    LB = "LB"
    KG = "KG"

    UNITS = [(KG, "Kilograms"), (LB, "Pounds")]

    exercise = models.ForeignKey(
        Exercise, related_name="sets", on_delete=models.CASCADE
    )
    repetitions = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    unit = models.CharField(max_length=32, choices=UNITS, default=LB)
    bodyweight = models.BooleanField(default=False)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Workout)
def set_workout_slug(sender, instance, **kwargs):
    if not instance.slug:
        h = hashids.Hashids(salt=settings.HASHIDS_SALT)
        instance.slug = h.encode(instance.id)
        instance.save()


@receiver(post_save, sender=Exercise)
def set_exercise_slug(sender, instance, **kwargs):
    if not instance.slug:
        h = hashids.Hashids(salt=settings.HASHIDS_SALT)
        instance.slug = h.encode(instance.id)
        instance.save()
