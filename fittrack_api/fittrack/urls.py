"""fittrack URL Configuration """
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns

from workouts.views import WorkoutList, WorkoutDetail

urlpatterns = [
    url(r'^workouts/$', WorkoutList.as_view()),
    url(r'^workouts/(?P<name>\w+)/$', WorkoutDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
