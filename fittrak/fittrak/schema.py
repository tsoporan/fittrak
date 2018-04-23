"""GraphQL Schema"""

import graphene
from graphene_django.debug import DjangoDebug

import workouts.schema


class Query(workouts.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello World"


schema = graphene.Schema(query=Query)
