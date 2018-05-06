"""Workouts GraphQL schema"""

import graphene

from graphene_django.types import DjangoObjectType

from workouts.models import Workout, Exercise, Set


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class Query(object):
    all_workouts = graphene.List(WorkoutType)
    all_exercises = graphene.List(ExerciseType)
    all_sets = graphene.List(SetType)

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()

    def resolve_all_sets(self, info, **kwargs):
        return Set.objects.all()
