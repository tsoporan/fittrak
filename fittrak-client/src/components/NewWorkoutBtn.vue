<template>
  <v-btn>Create Workout</v-btn>
</template>

<script>
import { queries, mutations } from "@/graphql";
import { showSnackbar } from "@/helpers";

import { IN_PROGRESS } from "@/constants";

export default {
  name: "CreateWorkout",

  data() {
    return {
      loading: false,
      dialog: false,
      exerciseTypes: [],
      searchSelectedExercises: [],
      selectedExercises: [],
      popularExerciseTypes: [],
      workout: null
    };
  },

  apollo: {
    exerciseTypes: {
      query: queries.exerciseTypesQuery,

      update(data) {
        return data.exerciseTypes;
      }
    },

    popularExerciseTypes: {
      query: queries.popularExerciseTypesQuery
    }
  },

  methods: {
    inSelected(exerciseId) {
      return Boolean(this.selectedExercises.find(ex => ex.id === exerciseId));
    },

    selectExercise(exercise) {
      if (this.inSelected(exercise.id)) {
        return;
      }
      this.selectedExercises = [exercise, ...this.selectedExercises];
    },

    deselectExercise(exerciseId) {
      this.selectedExercises = this.selectedExercises.filter(
        ex => ex.id !== exerciseId
      );
    },

    addMultiSelected() {
      const selectedWithIds = this.searchSelectedExercises.map(name => {
        const item = this.exerciseTypes.find(item => item.name === name);

        return {
          name,
          id: item.id
        };
      });

      this.selectedExercises = [...selectedWithIds, ...this.selectedExercises];

      this.searchSelectedExercises = [];
    },

    startWorkout() {
      const workout = this.workout;

      if (!this.selectedExercises.length) {
        showSnackbar("orange", "Uh-oh looks like you have no exercises added.");
        return;
      }

      if (!(workout && workout.id)) {
        showSnackbar(
          "error",
          "Hmm seems like there isn't an attached work out. Please create again."
        );
        return;
      }

      // Ensure matches the input type
      const normalizedSelected = this.selectedExercises.map(exercise => ({
        id: exercise.id,
        name: exercise.name
      }));

      this.$apollo
        .mutate({
          mutation: mutations.updateWorkoutMutation,

          variables: {
            workoutId: workout.id,
            workoutFields: {
              dateStarted: new Date(),
              status: IN_PROGRESS,
              exerciseTypes: normalizedSelected
            }
          }
        })
        .then(() => {
          this.selectedExercises = [];
          showSnackbar("success", "Workout started!");
        })
        .catch(() => {
          this.selectedExercises = [];
          showSnackbar("error", "Could not start workout.");
        });
    },

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
          this.loading = false;
          this.dialog = true;

          this.workout = resp.data.createWorkout.workout;
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
