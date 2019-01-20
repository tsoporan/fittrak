"""Workouts GraphQL Query"""

import graphene

from django.db.models import Count

from workouts.models import Exercise
from workouts.models import ExerciseType as ExerciseTypeModel
from workouts.models import MuscleGroup, Set, Workout

from .exercises import ExerciseType, ExerciseTypeType
from .helpers import get_object
from .sets import SetType
from .workouts import MuscleGroupType, WorkoutStatusesEnum, WorkoutType


class Query:
    workouts = graphene.List(
        WorkoutType,
        status=graphene.Argument(WorkoutStatusesEnum),
        limit=graphene.Int(required=False),
    )

    exercise_types = graphene.List(ExerciseTypeType)

    popular_exercise_types = graphene.List(ExerciseTypeType)

    exercises = graphene.List(ExerciseType, workout_id=graphene.Int(required=True))

    sets = graphene.List(SetType, exercise_id=graphene.Int(required=True))

    workout = graphene.Field(WorkoutType, workout_id=graphene.Int(required=True))

    exercise = graphene.Field(ExerciseType, exercise_id=graphene.Int(required=True))

    muscle_groups = graphene.List(MuscleGroupType)

    @staticmethod
    def resolve_muscle_groups(_, info):
        return MuscleGroup.objects.filter(is_active=True)

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
    def resolve_popular_exercise_types(_, info):
        user = info.context.user

        popular = (
            ExerciseTypeModel.objects.filter(is_active=True)
            .annotate(num_exercises=Count("exercise"))
            .order_by("-num_exercises")[:5]
        )

        return popular

    @staticmethod
    def resolve_exercises(_, info, workout_id):
        user = info.context.user

        return Exercise.objects.filter(is_active=True, workout_id=workout_id, user=user)

    @staticmethod
    def resolve_sets(_, info, exercise_id):
        user = info.context.user

        return Set.objects.filter(user=user, is_active=True, exercise_id=exercise_id)

    @staticmethod
    def resolve_workout(_, info, workout_id):
        user = info.context.user

        return get_object(Workout, {"id": workout_id, "user": user.id})

    @staticmethod
    def resolve_exercise(_, info, exercise_id):
        user = info.context.user

        return get_object(Exercise, {"id": exercise_id, "user": user.id})
