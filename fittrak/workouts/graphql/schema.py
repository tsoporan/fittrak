"""Workouts GraphQL schema"""

import graphene

from workouts.models import Workout, Exercise, Set

from .workouts import WorkoutType
from .exercises import ExerciseType
from .sets import SetType
from .helpers import get_object


class Query:
    all_workouts = graphene.List(WorkoutType)
    all_exercises = graphene.List(ExerciseType)
    all_sets = graphene.List(SetType)

    exercise = graphene.Field(
        ExerciseType,
        exercise_id=graphene.Int(required=True)
    )

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()

    def resolve_all_sets(self, info, **kwargs):
        return Set.objects.all()

    def resolve_exercise(self, info, exercise_id):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        return exercise
