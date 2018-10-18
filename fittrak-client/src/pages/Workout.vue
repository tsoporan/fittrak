<template>
  <v-container>
    <WorkoutDataContainer :workoutId="$route.params.workoutId">
      <template slot-scope="slotProps">
        <WorkoutHeader :workout="slotProps.workout" />
        <ExerciseActions :workout="slotProps.workout" />
        <ExerciseList :exercises="slotProps.exercises" />
      </template>
    </WorkoutDataContainer>
  </v-container>
</template>

<script>
import WorkoutDataContainer from "@/components/workouts/WorkoutDataContainer";
import WorkoutHeader from "@/components/workouts/WorkoutHeader";
import ExerciseActions from "@/components/exercises/ExerciseActions";
import ExerciseList from "@/components/exercises/ExerciseList";

export default {
  name: "Workout",

  components: {
    WorkoutDataContainer,
    WorkoutHeader,
    ExerciseActions,
    ExerciseList
  }
};
</script>

<style>
</style>
