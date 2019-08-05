<template>
  <v-flex xs6 text-xs-right>
    <v-btn
      :loading="loading"
      color="success"
      depressed
      @click.stop="startWorkout"
      >Start</v-btn
    >
  </v-flex>
</template>

<script>
import { mutations } from "@/graphql";

import { IN_PROGRESS } from "@/constants";
import { showSnackbar } from "@/helpers";

export default {
  name: "WorkoutStartButton",

  data() {
    return {
      loading: false
    };
  },

  methods: {
    startWorkout() {
      const { workout } = this.$props;

      this.loading = true;

      this.$apollo
        .mutate({
          mutation: mutations.updateWorkoutMutation,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              dateStarted: new Date(),
              status: IN_PROGRESS
            }
          }
        })
        .then(() => {
          this.loading = false;

          showSnackbar("success", "Workout started!");
        })
        .catch(() => {
          this.loading = false;

          showSnackbar(
            "error",
            "Oops, could not start workout. Support has been notified."
          );
        });
    }
  },

  props: {
    workout: {
      type: Object,
      required: true
    }
  }
};
</script>
