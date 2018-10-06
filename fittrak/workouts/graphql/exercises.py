"""
GraphQL Exercise types
"""

import graphene
from django.utils import timezone
from graphene_django.types import DjangoObjectType
from workouts.models import Exercise
from workouts.models import ExerciseType as ExerciseTypeModel
from workouts.models import MuscleGroup, Workout

from .helpers import get_object
from .workouts import WorkoutType


class ExerciseInputType(graphene.InputObjectType):
    name = graphene.String(required=True)


class ExerciseTypeType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = ExerciseTypeModel


class ExerciseType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = Exercise

    @staticmethod
    def resolve_name(instance, info):
        return instance.exercise_type.name


class AddCustomExercise(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercise_name = graphene.String(required=True)
        muscle_group_name = graphene.String(required=True)

    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, workout_id, exercise_name, muscle_group_name):
        user = info.context.user

        muscle_group = MuscleGroup.objects.get(
            name=muscle_group_name
        )

        exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
            user=user,
            name=exercise_name,
            muscle_group=muscle_group
        )

        workout = Workout.objects.get(id=workout_id)

        exercise = Exercise.objects.create(
            user=user,
            workout=workout,
            exercise_type=exercise_type
        )

        return AddCustomExercise(exercise=exercise)


class AddExercises(graphene.Mutation):
    class Arguments:
        workout_id = graphene.Int(required=True)
        exercises = graphene.List(ExerciseInputType, required=True)

    workout = graphene.Field(WorkoutType)
    exercises = graphene.List(ExerciseType)

    @staticmethod
    def mutate(_, info, workout_id, exercises):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        added = []

        for exercise in exercises:
            name = exercise["name"]

            # Allows for users to define their own exercise types based on name
            exercise_type, _ = ExerciseTypeModel.objects.get_or_create(
                user=user, name=name
            )

            exercise = Exercise.objects.create(
                user=user,
                workout=workout,
                exercise_type=exercise_type,
                date_started=timezone.now(),
            )

            added.append(exercise)

        return AddExercises(workout=workout, exercises=added)


class RemoveExercise(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)

    workout = graphene.Field(WorkoutType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        exercise.is_active = False
        exercise.save()

        return RemoveExercise(exercise=exercise, workout=exercise.workout)
