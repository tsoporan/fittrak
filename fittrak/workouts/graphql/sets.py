"""
GraphQL Set types
"""

import graphene
from django.utils import timezone
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

from workouts.models import Exercise, Set

from .exercises import ExerciseType
from .helpers import get_object
from .workouts import WorkoutType


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class SetFieldInputType(graphene.InputObjectType):
    weight = graphene.Int(required=True)
    repetitions = graphene.Int(required=True)
    unit = graphene.String(required=True)
    bodyweight = graphene.Boolean(required=False)


class AddSet(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.Int(required=True)
        repetitions = graphene.Int(required=True)
        weight = graphene.Int(required=True)
        unit = graphene.String(required=True)
        bodyweight = graphene.Boolean(default_value=False)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, exercise_id, repetitions, weight, unit, bodyweight):
        user = info.context.user

        exercise = get_object(Exercise, {"id": exercise_id, "user": user.id})

        if not exercise.workout:
            raise GraphQLError("Exercise does not belong to a workout.")

        _set = Set.objects.create(
            user=user,
            exercise=exercise,
            repetitions=repetitions,
            weight=weight,
            unit=unit,
            bodyweight=bodyweight,
        )

        return AddSet(set=_set, exercise=exercise)


class UpdateSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)
        set_fields = graphene.Argument(SetFieldInputType, required=True)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, set_id, set_fields):
        user = info.context.user

        _set = get_object(Set, {"id": set_id, "user": user.id})

        dirty = False
        for name, value in set_fields.items():
            if not hasattr(_set, name):
                continue

            setattr(_set, name, value)

            dirty = True

        if dirty:
            _set.updated_at = timezone.now()
            _set.save()

        return UpdateSet(set=_set, exercise=_set.exercise)


class RemoveSet(graphene.Mutation):
    class Arguments:
        set_id = graphene.Int(required=True)

    set = graphene.Field(SetType)
    exercise = graphene.Field(ExerciseType)

    @staticmethod
    def mutate(_, info, set_id):
        user = info.context.user

        _set = get_object(Set, {"id": set_id, "user": user.id})

        _set.is_active = False
        _set.updated_at = timezone.now()
        _set.save()

        return RemoveSet(set=_set, exercise=_set.exercise)
