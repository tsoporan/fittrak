<template>
  <div>
    <ul>
      <li v-for="exercise in exercises" :key="exercise.id">
          ID: {{ exercise.id }}
          Name: {{ exercise.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import VIEWER_WORKOUT from "@/graphql/queries/viewerWorkout.graphql";

export default {
  name: "ExerciseList",
  apollo: {
    exercises: {
      query: VIEWER_WORKOUT,
      variables() {
        return {
          workoutId: this.$route.params.workoutId
        };
      },
      update: data => data.viewer.workout.exercises
    }
  }
};
</script>
