"""
GraphQL Exercise types
"""

from django.utils import timezone

import graphene
from graphene_django.types import DjangoObjectType

from workouts.models import Workout, \
    Exercise, ExerciseType as ExerciseTypeModel

from .workouts import WorkoutType
from .helpers import get_object


class ExerciseType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = Exercise

    def resolve_name(instance, info):
        return instance.exercise_type.name


class AddExercise(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_name = graphene.String(required=True)

    workout = graphene.Field(WorkoutType)
    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, workout_id, exercise_name):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        # Allows for users to define their own exercise types based on name
        exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
            user=user,
            name=exercise_name
        )

        exercise = Exercise.objects.create(
            user=user,
            workout=workout,
            exercise_type=exercise_type,
            date_started=timezone.now()
        )

        return AddExercise(workout=workout, exercise=exercise)

