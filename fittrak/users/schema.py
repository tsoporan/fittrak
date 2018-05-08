""" Users GraphQL schema """

import uuid

from django.conf import settings
from django.db.models import Q

import graphene
from graphql import GraphQLError

from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Profile, NOT_SET, VERIFIED

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
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        User = get_user_model()

        exists = User.objects.filter(email=email).exists()

        if exists:
            raise GraphQLError("A user matching this criteria already exists.")

        new_user = User.objects.create_user(
            username = email,
            email = email,
            password = password,
            is_active = False
        )

        # Hook up the profile
        new_profile = Profile.objects.create(
            user = new_user,
            verification_token = uuid.uuid4().hex
        )

        return CreateUser(user=new_user)

class ActivateUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        verification_token = graphene.String(required=True)

    def mutate(self, info, verification_token):
        profile = Profile.objects.exclude(Q(verification_token=NOT_SET) |
                Q(verification_token=VERIFIED)).filter(verification_token=verification_token).first()

        if not profile:
            raise GraphQLError("No profile found.")

        user = profile.user
        user.is_active = True
        user.save()

        profile.verification_token = VERIFIED
        profile.save()

        return ActivateUser(ok=True)
