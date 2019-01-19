<template>
  <v-flex text-xs-right>
    <v-btn 
      icon
      dark
      color="primaryDark"
      @click.stop="createWorkout" 
      :loading="loading" 
    ><v-icon>add</v-icon>
    </v-btn>
  </v-flex>
</template>

<script>
import { mutations } from "@/graphql";
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
          mutation: mutations.createWorkoutMutation

          /*
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
          */
        })
        .then(resp => {
          const workout = resp.data.createWorkout.workout;

          this.loading = false;

          showSnackbar("success", "New workout created.");

          this.$router.push({
            name: "Workout",
            params: { workoutId: workout.id }
          });
        })
        .catch(() => {
          this.loading = false;

          showSnackbar(
            "error",
            "Oops, there seems to be a problem, support has been notified."
          );
        });
    }
  }
};
</script>
