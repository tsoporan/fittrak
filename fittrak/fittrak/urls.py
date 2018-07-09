"""fittrak URL Configuration """
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView

from .schema import schema

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema))),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', login_required(
        TemplateView.as_view(template_name='index.html')), name="index"),
    url(r'^.*', login_required(
        TemplateView.as_view(template_name='index.html')
    ))
]
