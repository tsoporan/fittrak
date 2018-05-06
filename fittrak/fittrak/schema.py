"""Root GraphQL Schema"""

import graphene

from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug

import users.schema
import workouts.schema


class RootQuery(workouts.schema.Query, users.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class RootMutation(graphene.ObjectType):
    create_user = users.schema.CreateUser.Field()

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
