"""Workouts GraphQL schema"""

import graphene
from workouts.models import Exercise
from workouts.models import ExerciseType as ExerciseTypeModel
from workouts.models import Workout

from .exercises import ExerciseType, ExerciseTypeType
from .helpers import get_object
from .workouts import WorkoutStatusesEnum, WorkoutType


class Query:
    workouts = graphene.List(
        WorkoutType,
        status=graphene.Argument(WorkoutStatusesEnum),
        limit=graphene.Int(required=False),
    )

    workout = graphene.Field(WorkoutType, workout_id=graphene.Int(required=True))

    exercise = graphene.Field(ExerciseType, exercise_id=graphene.Int(required=True))

    exercise_types = graphene.List(ExerciseTypeType)

    @staticmethod
    def resolve_workouts(_, info, status=None, limit=None):
        user = info.context.user

        filter_args = {"user": user, "is_active": True}

        if status:
            filter_args["status"] = status

        qs = Workout.objects.filter(**filter_args)

        if limit and limit > 0:
            qs = qs[:limit]

        return qs

    @staticmethod
    def resolve_exercise_types(_, info):
        user = info.context.user

        user_types = ExerciseTypeModel.objects.filter(user=user, is_active=True)
        all_types = ExerciseTypeModel.objects.filter(is_active=True).exclude(user=user)

        return user_types | all_types

    @staticmethod
    def resolve_workout(_, info, workout_id):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        return workout

    @staticmethod
    def resolve_exercise(_, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        return exercise
