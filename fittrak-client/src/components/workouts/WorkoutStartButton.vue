<template>
  <v-flex xs6 text-xs-right>
    <v-btn :loading="loading" color="success" depressed @click.stop="startWorkout">Start</v-btn>

    <ErrorSnackbar v-if="error" :text="errorText" />
  </v-flex>
</template>

<script>
import UpdateWorkoutMutation from "@/graphql/mutations/updateWorkout.graphql";

import ErrorSnackbar from "@/components/app/ErrorSnackbar";

import { IN_PROGRESS } from "@/constants";

export default {
  name: "WorkoutStartButton",

  data() {
    return {
      loading: false,
      error: false,
      errorText: ""
    };
  },

  methods: {
    startWorkout() {
      const { workout } = this.$props;

      this.loading = true;
      this.error = false;

      this.$apollo
        .mutate({
          mutation: UpdateWorkoutMutation,

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
        })
        .catch(() => {
          this.loading = false;
          this.error = true;
          this.errorText =
            "Oops, could not start workout. Support has been notified.";
        });
    }
  },

  props: {
    workout: Object
  },

  components: {
    ErrorSnackbar
  }
};
</script>
