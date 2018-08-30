"""Workouts GraphQL schema"""

import graphene

from workouts.models import Workout, Exercise, Set, IN_PROGRESS

from .workouts import WorkoutType, WorkoutStatusesEnum
from .exercises import ExerciseType
from .sets import SetType
from .helpers import get_object


class Query:
    workouts = graphene.List(
        WorkoutType,
        status=graphene.Argument(WorkoutStatusesEnum),
        limit=graphene.Int(required=False))

    workout = graphene.Field(
        WorkoutType, workout_id=graphene.Int(required=True))

    exercise = graphene.Field(
        ExerciseType, exercise_id=graphene.Int(required=True))

    def resolve_workouts(self, info, status=None, limit=None):
        user = info.context.user

        filter_args = {
            "user": user,
            "is_active": True,
        }

        if status:
            filter_args["status"] = status

        qs = Workout.objects.filter(**filter_args)

        if limit and limit > 0:
            qs = qs[:limit]

        return qs

    def resolve_workout(self, info, workout_id):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        return workout

    def resolve_exercise(self, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        return exercise
