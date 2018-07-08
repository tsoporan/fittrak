""" Users GraphQL schema """

from django.contrib.auth import get_user_model

import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType

from .models import Profile

from workouts.models import Workout

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Viewer(DjangoObjectType):
    profile = graphene.Field(ProfileType)
    workouts = graphene.List("workouts.schema.WorkoutType")

    class Meta:
        model = get_user_model()

    def resolve_workouts(self, info):
        user = info.context.user

        return Workout.objects.filter(
            user = user,
            is_active = True
        )


class Query:
    viewer = graphene.Field(Viewer)

    def resolve_viewer(self, info):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not authenticated.")

        return user
