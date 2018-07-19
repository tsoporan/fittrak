"""Workouts GraphQL schema"""

import graphene

from workouts.models import Workout, Exercise, Set

from .workouts import WorkoutType
from .exercises import ExerciseType
from .sets import SetType
from .helpers import get_object


class Query:
    workouts = graphene.List(WorkoutType)

    workout = graphene.Field(
        WorkoutType,
        workout_id=graphene.Int(required=True)
    )

    exercise = graphene.Field(
        ExerciseType,
        exercise_id=graphene.Int(required=True)
    )

    def resolve_workouts(self, info):
        user = info.context.user

        return Workout.objects.filter(
            user=user,
            is_active=True
        )

    def resolve_workout(self, info, workout_id):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        return workout


    def resolve_exercise(self, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        return exercise
