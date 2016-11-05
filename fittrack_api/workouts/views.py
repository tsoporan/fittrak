from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from django.http import Http404

from .serializers import WorkoutSerializer, ExerciseSerializer
from .models import Workout, Exercise

class ExerciseList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all exercises
        """
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetail(APIView):
    """
    Retrieve, update or delete a Workout
    """

    def get_object(self, slug):
        try:
            return Exercise.objects.get(slug=slug)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        exercise = self.get_object(slug)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        exercise = self.get_object(name)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        exercise = self.get_object(slug)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkoutList(APIView):
    """ 
    Display list of Workouts
    """

    #authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        """
        Return a list of all workouts.
        """
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    """
    Retrieve, update or delete a Workout
    """

    def get_object(self, name):
        try:
            return Workout.objects.get(display_name=name)
        except Workout.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        workout = self.get_object(name)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        workout = self.get_object(name)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        workout = self.get_object(slug)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
