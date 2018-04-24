"""fittrak URL Configuration """
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

if not settings.DEBUG:
    csrf_exempt = lambda x: x

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
