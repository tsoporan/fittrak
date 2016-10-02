from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import WorkoutSerializer
from .models import Workout

class WorkoutList(APIView):

    #authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        """
        Return a list of all workouts.
        """
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

class WorkoutDetail(APIView):
    pass
