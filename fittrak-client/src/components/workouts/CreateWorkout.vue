<template>
  <v-btn
    fab
    small
    color="darkGrey"
    @click.stop="createWorkout"
    :loading="loading"
  >
    <v-icon>add</v-icon>
  </v-btn>
</template>

<script>
import { queries, mutations } from "@/graphql";
import { showSnackbar } from "@/helpers";

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
          mutation: mutations.createWorkoutMutation,

          update: (store, { data }) => {
            const newWorkout = data.createWorkout.workout;
            const result = store.readQuery({
              query: queries.workoutsQuery
            });

            // Prepend the latest workout
            result.workouts.unshift(newWorkout);

            store.writeQuery({
              query: queries.workoutsQuery,
              data: result
            });
          }
        })
        .then(resp => {
          const { workout } = resp.data.createWorkout;

          this.$router.push({
            name: "WorkoutSetup",
            params: {
              workoutId: workout.id
            }
          });
        })
        .catch(() => {
          this.loading = false;

          showSnackbar(
            "error",
            "Oops, there seems to have been a problem creating your workout."
          );
        });
    }
  }
};
</script>
