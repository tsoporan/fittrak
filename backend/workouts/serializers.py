from rest_framework import serializers
from .models import Workout, Exercise, Set, ExerciseType, WorkoutStatus


class SetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_started = serializers.DateTimeField()
    date_ended = serializers.DateTimeField()
    repetitions = serializers.IntegerField()
    weight = serializers.IntegerField()
    unit = serializers.CharField(max_length=4)

    def create(self, validated_data):
        """ Create new Set based on valid data """
        return Set.objects.create(**validated_data)


class ExerciseTypeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=15)


class ExerciseSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_started = serializers.DateTimeField()
    date_ended = serializers.DateTimeField()
    slug = serializers.CharField(max_length=15)
    type = ExerciseTypeSerializer(read_only=True)
    sets = SetSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """ Create new Exercise based on valid data """
        return Exercise.objects.create(**validated_data)

class WorkoutStatusSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=15)

class WorkoutSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_started = serializers.DateTimeField()
    date_ended = serializers.DateTimeField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    slug = serializers.CharField(max_length=15)
    is_active = serializers.BooleanField()
    exercises = ExerciseSerializer(many=True, read_only=True)
    status = WorkoutStatusSerializer()

    def create(self, validated_data):
        """ Create new Workout based on valid data """
        return Workout.objects.create(**validated_data)

