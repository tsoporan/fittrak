"""
GraphQL Workout types
"""

from graphql import GraphQLError

import graphene
from graphene_django.types import DjangoObjectType

from django.utils import timezone

from workouts.models import Workout, PENDING, IN_PROGRESS, CANCELLED, COMPLETE

from .helpers import get_object


class WorkoutStatusesEnum(graphene.Enum):
    PENDING = PENDING
    IN_PROGRESS = IN_PROGRESS
    CANCELLED = CANCELLED
    COMPLETE = COMPLETE


class WorkoutFieldInputType(graphene.InputObjectType):
    date_started = graphene.types.datetime.DateTime()
    date_ended = graphene.types.datetime.DateTime()
    status = graphene.Field(WorkoutStatusesEnum)


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class CreateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    def mutate(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not authenticated.")

        new_workout = Workout.objects.create(
            user=user, date_started=timezone.now())

        return CreateWorkout(workout=new_workout)


class RemoveWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)

    def mutate(self, info, workout_id):
        user = info.context.user

        workout = get_object(Workout, {"id": workout_id, "user": user.id})
        workout.updated_at = timezone.now()
        workout.is_active = False
        workout.save()

        return RemoveWorkout(workout=workout)


class UpdateWorkout(graphene.Mutation):
    workout = graphene.Field(WorkoutType)

    class Arguments:
        workout_id = graphene.Int(required=True)
        workout_fields = graphene.Argument(
            WorkoutFieldInputType, required=True)

    def mutate(self, info, workout_id, workout_fields):
        user = info.context.user
        workout = get_object(Workout, {"id": workout_id, "user": user.id})

        dirty = False
        # Unpack the fields and update the model
        for name, value in workout_fields.items():
            if not hasattr(workout, name):
                continue

            setattr(workout, name, value)
            dirty = True

        if dirty:
            workout.updated_at = timezone.now()
            workout.save()

        return UpdateWorkout(workout=workout)
