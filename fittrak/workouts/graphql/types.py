"""
Workout GraphQL types
"""

import graphene
from graphene_django.types import DjangoObjectType
from workouts.models import Exercise
from workouts.models import ExerciseType as ExerciseTypeModel
from workouts.models import MuscleGroup, Set, Workout


class MuscleGroupType(DjangoObjectType):
    class Meta:
        model = MuscleGroup


class WorkoutStatusesEnum(graphene.Enum):
    IN_PROGRESS = Workout.IN_PROGRESS
    COMPLETE = Workout.COMPLETE
    CANCELLED = Workout.CANCELLED
    PAUSED = Workout.PAUSED


class ExerciseTypeType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = ExerciseTypeModel


class ExerciseTypeInputType(graphene.InputObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)


class WorkoutFieldInputType(graphene.InputObjectType):
    started_at = graphene.types.datetime.DateTime()
    ended_at = graphene.types.datetime.DateTime()

    # Only allowed status changes from client
    # i.e pending and archive are reserved for creation and "removal"
    status = graphene.Field(WorkoutStatusesEnum)
    exercise_types = graphene.List(ExerciseTypeInputType)


class WorkoutType(DjangoObjectType):
    exercise_count = graphene.Int()

    class Meta:
        model = Workout

    @staticmethod
    def resolve_exercise_count(workout, info):
        return workout.exercises.count()


class ExerciseInputType(graphene.InputObjectType):
    name = graphene.String(required=True)


class ExerciseType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = Exercise

    @staticmethod
    def resolve_name(instance, info):
        return instance.exercise_type.name


class SetType(DjangoObjectType):
    class Meta:
        model = Set


class SetFieldInputType(graphene.InputObjectType):
    weight = graphene.Decimal(required=True)
    repetitions = graphene.Int(required=True)
    unit = graphene.String(required=True)
    bodyweight = graphene.Boolean(required=False)
