<template>
  <v-flex xs6 text-xs-right>
    <v-btn :loading="loading" large @click.stop="createWorkout" class="success">
      Create Workout
    </v-btn>

    <ErrorSnackbar v-if="error" :text="errorText" />
  </v-flex>
</template>

<script>
import WorkoutsQuery from "@/graphql/queries/workouts.graphql";
import CreateWorkoutMutation from "@/graphql/mutations/createWorkout.graphql";

import ErrorSnackbar from "@/components/app/ErrorSnackbar";

export default {
  name: "CreateWorkout",

  data() {
    return {
      error: false,
      errorText: "",
      loading: false
    };
  },

  methods: {
    createWorkout() {
      this.error = false;
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
          this.$router.push({
            name: "WorkoutDetail",
            params: { workoutId: workout.id }
          });
        })
        .catch(() => {
          this.loading = false;
          this.error = true;
          this.errorText =
            "Oops, there seems to be a problem, support has been notified.";
        });
    }
  },

  components: {
    ErrorSnackbar
  }
};
</script>
