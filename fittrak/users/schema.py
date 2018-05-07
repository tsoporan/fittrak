""" Users GraphQL schema """

import uuid

from django.conf import settings
from django.db.models import Q

import graphene
from graphql import GraphQLError

from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Profile

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Viewer(DjangoObjectType):
    profile = graphene.Field(ProfileType)

    class Meta:
        model = get_user_model()


class Query:
    viewer = graphene.Field(Viewer)

    def resolve_viewer(self, info):
        user = info.context.user

        if not user.is_authenticated:
            return None

        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(Viewer)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password):
        User = get_user_model()

        exists = User.objects.filter(email=email).exists()

        if exists:
            raise GraphQLError("A user matching this criteria already exists.")

        new_user = User.objects.create_user(
            username = email,
            email = email,
            password = password
        )

        # Hook up the profile
        new_profile = Profile.objects.create(
            user = new_user,
            verification_token = uuid.uuid4().hex
        )

        return CreateUser(user=new_user)
