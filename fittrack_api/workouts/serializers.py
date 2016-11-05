from rest_framework import serializers
from .models import Workout, Exercise, Set

class WorkoutSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_started = serializers.DateTimeField()
    date_ended = serializers.DateTimeField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    slug = serializers.CharField(max_length=15)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        """ Create new Workout based on valid data """
        return Workout.objects.create(**validated_data)

class ExerciseSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_started = serializers.DateTimeField()
    date_ended = serializers.DateTimeField()
    user = serializers.IntegerField(allow_null=True)
    slug = serializers.CharField(max_length=15)
    name = serializers.CharField()

    def create(self, validated_data):
        """ Create new Exercise based on valid data """
        return Exercise.objects.create(**validated_data)

class SetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    started = serializers.DateTimeField()
    ended = serializers.DateTimeField()
    user = serializers.IntegerField()

    def create(self, validated_data):
        """ Create new Set based on valid data """
        return Set.objects.create(**validated_data)
