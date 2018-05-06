""" Users GraphQL schema """

from django.conf import settings
from django.db.models import Q

import graphene
from graphql import GraphQLError

from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

class Viewer(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL
        only_fields = ('id', 'email', 'username', 'date_joined', 'is_active')

class CreateUser(graphene.Mutation):
    user = graphene.Field(Viewer)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, email, password):
        user = info.context.user

        User = get_user_model()

        if user.is_authenticated:
            raise GraphQLError("Cannot create a user when logged in.")

        exists = User.objects.filter(Q(email=email) | Q(username=username)).exists()

        if exists:
            raise GraphQLError("A user matching this criteria already exists.")

        new_user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        return CreateUser(user=new_user)

class Query:
    viewer = graphene.Field(Viewer)

    def resolve_viewer(self, info):
        user = info.context.user
        print ("info context", info.context.user)

        if not user.is_authenticated:
            return None

        return user
