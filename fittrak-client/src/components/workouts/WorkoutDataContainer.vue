<template>
<v-layout row wrap>
  <slot name="header" :workout="workout"></slot>
  <slot name="form" :workout="workout"></slot>
  <slot name="list" :exercises="workout.exercises"></slot>
</v-layout>
</template>

<script>
import WorkoutQuery from "@/graphql/queries/workout.graphql";

export default {
  name: "WorkoutDataContainer",

  data() {
    return {
      workout: {}
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
      update: data => {
        return data.workout;
      }
    }
  },

  props: {
    workoutId: String
  }
};
</script>
