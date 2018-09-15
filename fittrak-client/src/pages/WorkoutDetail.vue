<template>
<v-container>
  <WorkoutDataContainer :workoutId="$route.params.workoutId">
    <WorkoutDetailHeader slot="header" slot-scope="workout" :status="workout.status" />
    <AddExercise slot="form" slot-scope="workout" :workout="workout.workout" />
    <ExerciseList slot="list" slot-scope="workout" :exercises="workout.exercises" />
  </WorkoutDataContainer>
</v-container>
</template>

<script>
import WorkoutDataContainer from "@/components/workouts/WorkoutDataContainer";
import WorkoutDetailHeader from "@/components/workouts/WorkoutDetailHeader";
import AddExercise from "@/components/exercises/AddExercise";
import ExerciseList from "@/components/exercises/ExerciseList";

export default {
  name: "WorkoutDetail",

  components: {
    WorkoutDataContainer,
    WorkoutDetailHeader,
    AddExercise,
    ExerciseList
  }
};
</script>

<style>
</style>
