<template>
  <v-layout 
    row 
    wrap>
    <slot 
      name="header" 
      :workout="workout"/>
    <slot 
      name="actions" 
      :workout="workout"/>
    <slot 
      name="list" 
      :exercises="exercises"/>
  </v-layout>
</template>

<script>
import WorkoutQuery from "@/graphql/queries/workout.graphql";
import ExercisesQuery from "@/graphql/queries/exercises.graphql";

export default {
  name: "WorkoutDataContainer",

  data() {
    return {
      workout: {},
      exercises: []
    };
  },

  apollo: {
    workout: {
      query: WorkoutQuery,
      variables() {
        return {
          workoutId: this.$props.workoutId
        };
      },
      update: data => data.workout
    },
    exercises: {
      query: ExercisesQuery,
      variables() {
        return {
          workoutId: this.$props.workoutId
        };
      },
      update: data => data.exercises
    }
  },

  props: {
    workoutId: String
  }
};
</script>
