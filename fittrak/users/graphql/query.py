""" Users GraphQL Query"""

import graphene

from graphql import GraphQLError

from .types import Viewer


class Query:
    viewer = graphene.Field(Viewer)

    @staticmethod
    def resolve_viewer(_, info):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not authenticated.")

        return user
