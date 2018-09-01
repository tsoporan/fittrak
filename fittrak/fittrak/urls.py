"""fittrak URL Configuration """
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

from .schema import schema
from .views import index


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


if not settings.DEBUG:
    csrf_exempt = lambda x: x

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^accounts/", include("registration.backends.simple.urls")),
    url(
        r"^graphql",
        csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema)),
    ),
    url(r"^$", index, name="index"),
    url(r"^.*", index),
]
