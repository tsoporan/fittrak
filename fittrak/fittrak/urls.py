"""fittrak URL Configuration """
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from graphene_django.views import GraphQLView

if not settings.DEBUG:
    csrf_exempt = lambda x: x

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', login_required(csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG)))),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', login_required(
        TemplateView.as_view(template_name='index.html'))
        ),
]
