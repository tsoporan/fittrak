import hashids
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from fittrak.utils.models import UserBaseModel


class Workout(UserBaseModel):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    ARCHIVED = "ARCHIVED"
    PAUSED = "PAUSED"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (CANCELLED, "Cancelled"),
        (COMPLETE, "Complete"),
        (ARCHIVED, "Archived"),
        (PAUSED, "Paused"),
    )

    slug = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="A human easy to read/share name for workout",
    )

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=PENDING)

    started_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp workout started"
    )

    ended_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp workout ended"
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"#{self.id}-{self.slug} - {self.user}"

    def is_finished(self):
        return True if self.ended_at else False


class WorkoutEvent(UserBaseModel):
    """
    Tracks state change on a Workout
    """

    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    action = models.CharField(max_length=64)

    # DjangoJSONEncoder deals with datetimes and uuids, default encoder does not
    state = JSONField(encoder=DjangoJSONEncoder, help_text="Store the model state")

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.workout}"


class MuscleGroup(UserBaseModel):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name


class ExerciseType(UserBaseModel):
    name = models.CharField(max_length=250)
    muscle_group = models.ForeignKey(
        MuscleGroup, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("user", "name")
        ordering = ("-id",)

    def __str__(self):
        return self.name


class Exercise(UserBaseModel):
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

    started_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp Exercise started"
    )

    ended_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp Exercise ended"
    )

    duration = models.DurationField(null=True, blank=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.exercise_type.name


class Set(UserBaseModel):
    LB = "LB"
    KG = "KG"

    UNITS = [(KG, "Kilograms"), (LB, "Pounds")]

    exercise = models.ForeignKey(
        Exercise, related_name="sets", on_delete=models.CASCADE
    )
    repetitions = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    unit = models.CharField(max_length=2, choices=UNITS, default=LB)
    bodyweight = models.BooleanField(default=False)

    started_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp Set started"
    )

    ended_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp Set ended"
    )

    duration = models.DurationField(null=True, blank=True)

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
