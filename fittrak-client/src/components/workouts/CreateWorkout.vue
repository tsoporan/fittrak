<template>
  <v-flex xs6 text-xs-right>
    <v-btn :loading="loading" large @click.stop="createWorkout" class="success">
      Create Workout
    </v-btn>
  </v-flex> 
</template>

<script>
import WorkoutsQuery from "@/graphql/queries/workouts.graphql";
import CreateWorkoutMutation from "@/graphql/mutations/createWorkout.graphql";

import { EventBus } from "@/helpers";

export default {
  name: "CreateWorkout",

  data() {
    return {
      loading: false
    };
  },

  methods: {
    createWorkout() {
      this.loading = true;

      this.$apollo
        .mutate({
          mutation: CreateWorkoutMutation,

          update: (store, { data }) => {
            const newWorkout = data.createWorkout.workout;
            const result = store.readQuery({
              query: WorkoutsQuery
            });

            // Prepend the latest workout
            result.workouts.unshift(newWorkout);

            store.writeQuery({
              query: WorkoutsQuery,
              data: result
            });
          }
        })
        .then(resp => {
          const workout = resp.data.createWorkout.workout;

          this.loading = false;

          EventBus.$emit("show-snackbar", {
            text: "New workout created.",
            type: "success"
          });

          this.$router.push({
            name: "Workout",
            params: { workoutId: workout.id }
          });
        })
        .catch(() => {
          this.loading = false;

          EventBus.$emit("show-snackbar", {
            text:
              "Oops, there seems to be a problem, support has been notified.",
            type: "error"
          });
        });
    }
  }
};
</script>
