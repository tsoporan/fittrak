<template>
  <v-flex xs6 text-xs-right>
    <v-btn :loading="loading" large @click.stop="createWorkout" class="success">
      Create Workout
    </v-btn>

    <v-snackbar
      v-model="snackbar.open"
      :timeout="snackbar.timeout"
      :bottom="true"
      :color="snackbar.color"
    >
      {{ snackbar.text }}
      <v-btn
        flat
        @click="snackbar.open = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-flex>
</template>

<script>
import WORKOUTS from "@/graphql/queries/workouts.graphql";
import CREATE_WORKOUT from "@/graphql/mutations/createWorkout.graphql";

export default {
  name: "CreateWorkout",

  data() {
    return {
      snackbar: {
        open: false,
        text: "",
        timeout: 7000,
        color: "error"
      },
      loading: false
    };
  },

  methods: {
    createWorkout() {
      this.loading = true;

      this.$apollo
        .mutate({
          mutation: CREATE_WORKOUT,

          update: (store, { data }) => {
            const newWorkout = data.createWorkout.workout;
            const result = store.readQuery({
              query: WORKOUTS
            });

            // Prepend the latest workout
            result.workouts.unshift(newWorkout);

            store.writeQuery({
              query: WORKOUTS,
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
          this.snackbar.open = true;
          this.snackbar.text =
            "Oops, there seems to be a problem, support has been notified.";
        });
    }
  }
};
</script>
