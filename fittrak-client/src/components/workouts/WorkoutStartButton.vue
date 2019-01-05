<template>
  <v-flex 
    xs6 
    text-xs-right>
    <v-btn 
      :loading="loading" 
      color="success" 
      depressed 
      @click.stop="startWorkout">Start</v-btn>
  </v-flex>
</template>

<script>
import UpdateWorkoutMutation from "@/graphql/mutations/updateWorkout.graphql";

import { IN_PROGRESS } from "@/constants";
import { EventBus } from "@/helpers";

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

          EventBus.$emit("show-snackbar", {
            type: "success",
            text: "Workout started!"
          });
        })
        .catch(() => {
          this.loading = false;

          EventBus.$emit("show-snackbar", {
            type: "error",
            text: "Oops, could not start workout. Support has been notified."
          });
        });
    }
  },

  props: {
    workout: Object
  }
};
</script>
