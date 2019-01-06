""" Users GraphQL schema """

import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

from .models import Profile


class UnitEnumType(graphene.Enum):
    LBS = Profile.LBS
    KGS = Profile.KGS


class ProfileType(DjangoObjectType):
    preferred_unit = graphene.Field(UnitEnumType)

    class Meta:
        model = Profile


class Viewer(DjangoObjectType):
    profile = graphene.Field(ProfileType)

    class Meta:
        model = get_user_model()
        only_fields = ("id", "username", "email")


class Query:
    viewer = graphene.Field(Viewer)

    @staticmethod
    def resolve_viewer(_, info):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not authenticated.")

        return user
