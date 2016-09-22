from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Workout, Exercise, Set

@login_required
def new_workout(request):
    return render(request, 'workouts/new_workout.html')

