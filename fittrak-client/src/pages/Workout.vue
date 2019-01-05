<template>
  <v-container>
    <WorkoutDataContainer :workout-id="$route.params.workoutId">
      <WorkoutHeader 
        slot="header" 
        slot-scope="data" 
        :workout="data.workout" />
      <ExerciseActions 
        slot="actions" 
        slot-scope="data" 
        :workout="data.workout" />
      <ExerciseList 
        slot="list" 
        slot-scope="data" 
        :exercises="data.exercises" />
    </WorkoutDataContainer>
  </v-container>
</template>

<script>
import WorkoutDataContainer from "@/components/workouts/WorkoutDataContainer";
import WorkoutHeader from "@/components/workouts/WorkoutHeader";
import ExerciseActions from "@/components/exercises/ExerciseActions";
import ExerciseList from "@/components/exercises/ExerciseList";

export default {
  name: "WorkoutDetail",

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
