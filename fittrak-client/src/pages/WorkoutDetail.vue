<template>
<v-container>
  <WorkoutDataContainer :workoutId="$route.params.workoutId">
    <WorkoutDetailHeader slot="header" slot-scope="data" :workout="data.workout" />
    <AddExercise slot="form" slot-scope="data" :workout="data.workout" />
    <ExerciseList slot="list" slot-scope="data" :exercises="data.exercises" />
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
