"""fittrack URL Configuration """
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from graphene_django.views import GraphQLView

from workouts.views import \
    WorkoutList, WorkoutDetail, ExerciseList, ExerciseDetail

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^workouts/$', WorkoutList.as_view()),
    url(r'^workouts/(?P<slug>\w+)/$', WorkoutDetail.as_view()),
    url(r'^exercises/$', ExerciseList.as_view()),
    url(r'^exercises/(?P<slug>\w+)/$', ExerciseDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
