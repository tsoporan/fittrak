<template>
  <v-flex text-xs-right>
    <v-btn :loading="loading" color="info" depressed @click.stop="finishWorkout">Finish</v-btn>
  </v-flex>
</template>

<script>
import UpdateWorkoutMutation from "@/graphql/mutations/updateWorkout.graphql";

import { COMPLETE } from "@/constants";
import { EventBus } from "@/helpers";

export default {
  name: "WorkoutFinishButton",

  data() {
    return {
      loading: false
    };
  },

  methods: {
    finishWorkout() {
      const { workout } = this.$props;

      this.loading = true;

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
            name: "FitTrak"
          });

          EventBus.$emit("show-snackbar", {
            text: "Workout finished.",
            type: "success"
          });
        })
        .catch(() => {
          this.loading = false;

          EventBus.$emit("show-snackbar", {
            text: "Oops, could not finish workout. Support has been notified.",
            type: "error"
          });
        });
    }
  },

  props: {
    workout: Object
  }
};
</script>
