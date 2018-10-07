<template>
  <v-flex text-xs-right>
    <v-btn :loading="loading" color="info" depressed @click.stop="finishWorkout">Finish</v-btn>

    <ErrorSnackbar v-if="error" :text="errorText" />
  </v-flex>
</template>

<script>
import UpdateWorkoutMutation from "@/graphql/mutations/updateWorkout.graphql";

import ErrorSnackbar from "@/components/app/ErrorSnackbar";

import { COMPLETE } from "@/constants";

export default {
  name: "WorkoutFinishButton",

  data() {
    return {
      loading: false,
      error: false,
      errorText: ""
    };
  },

  methods: {
    finishWorkout() {
      const { workout } = this.$props;

      this.loading = true;
      this.error = false;

      this.$apollo
        .mutate({
          mutation: UpdateWorkoutMutation,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              dateEnded: new Date(),
              status: COMPLETE
            }
          }
        })
        .then(() => {
          this.loading = false;

          this.$router.push({
            name: "Home"
          });
        })
        .catch(() => {
          this.loading = false;
          this.error = true;
          this.errorText =
            "Oops, could not finish workout. SUpport has been notified.";
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
