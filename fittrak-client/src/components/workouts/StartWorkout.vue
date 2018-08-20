<template>
  <button class="button is-primary" v-on:click="startWorkout">Start Workout</button>
</template>

<script>
import UPDATE_WORKOUT from "@/graphql/mutations/updateWorkout.graphql";
import { IN_PROGRESS } from "@/constants";

export default {
  name: "StartWorkout",
  methods: {
    startWorkout() {
      const { workout } = this.$props;

      this.$apollo.mutate({
        mutation: UPDATE_WORKOUT,

        variables: {
          workoutId: workout.id,
          workoutFields: {
            dateStarted: new Date(),
            status: IN_PROGRESS
          }
        }
      });
    }
  },

  props: {
    workout: Object
  }
};
</script>
