"""
GraphQL Set types
"""

from django.utils import timezone

from graphql import GraphQLError

import graphene
from graphene_django.types import DjangoObjectType

from workouts.models import Exercise, Set

from .workouts import WorkoutType
from .exercises import ExerciseType
from .helpers import get_object


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class SetFieldInputType(graphene.InputObjectType):
    weight = graphene.Int()
    repetitions = graphene.Int()
    unit = graphene.String()


class AddSet(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)
        repetitions = graphene.Int(required=True)
        weight = graphene.Int(required=True)
        unit = graphene.String()

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)
    workout = graphene.Field(WorkoutType)

    def mutate(self, info, exercise_id, repetitions, weight, unit):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        if not exercise.workout:
            raise GraphQLError("Exercise does not belong to a workout.")

        set = Set.objects.create(
            user=user,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight
        )

        return AddSet(set=set, exercise=exercise, workout=exercise.workout)


class UpdateSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)
        set_fields = graphene.Argument(
            SetFieldInputType,
            required=True
        )

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, set_id, set_fields):
        user = info.context.user

        set = get_object(Set, {"id": set_id, "user": user.id})

        dirty = False
        for name, value in set_fields.items():
            if not hasattr(set, name):
                continue

            setattr(set, name, value)

            dirty = True

        if dirty:
            set.updated_at = timezone.now()
            set.save()

        return UpdateSet(set=set, exercise=set.exercise)


class RemoveSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, set_id):
        user = info.context.user

        set = get_object(Set, {"id": set_id, "user": user.id})

        set.is_active = False
        set.updated_at = timezone.now()
        set.save()

        return RemoveSet(set=set, exercise=set.exercise)
