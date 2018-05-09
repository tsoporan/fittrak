"""Workouts GraphQL schema"""

import graphene

from django.utils import timezone

from graphql import GraphQLError

from graphene_django.types import DjangoObjectType

from .models import Workout, Exercise, Set

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class Query:
    all_workouts = graphene.List(WorkoutType)
    all_exercises = graphene.List(ExerciseType)
    all_sets = graphene.List(SetType)

    def resolve_all_workouts(self, info, **kwargs):
        return Workout.objects.all()

    def resolve_all_exercises(self, info, **kwargs):
        return Exercise.objects.select_related('workout').all()

    def resolve_all_sets(self, info, **kwargs):
        return Set.objects.all()

class CreateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    def mutate(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not authenticated.")

        new_workout = Workout.objects.create(
            user = user,
            date_started = timezone.now()
        )

        return CreateWorkout(workout=new_workout)
