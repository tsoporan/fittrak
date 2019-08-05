<template>
  <v-flex xs12>
    <v-form class="ma-4">
      <v-autocomplete
        v-model="newExercises"
        :items="exerciseTypes"
        placeholder="Select exercises ..."
        browser-autcomplete
        clearable
        chips
        deletable-chips
        hint
        multiple
        small-chips
      />

      <v-btn @click.stop="addExercises" :disabled="!newExercises.length">
        Add Exercises
      </v-btn>

      <AddCustomExercise :workout="workout" />
    </v-form>
  </v-flex>
</template>

<script>
import { queries, mutations } from "@/graphql";

import AddCustomExercise from "@/components/exercises/AddCustomExercise";

import { showSnackbar } from "@/helpers";

export default {
  name: "AddExerciseForm",

  data: () => ({
    newExercises: [],
    exerciseTypes: []
  }),

  apollo: {
    exerciseTypes: {
      query: queries.exerciseTypesQuery,
      update: data => data.exerciseTypes.map(exerciseType => exerciseType.name)
    }
  },

  methods: {
    addExercises() {
      const workout = this.workout;

      if (!this.newExercises.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: mutations.addExercisesMutation,

          variables: {
            workoutId: workout.id,
            exercises: this.newExercises.map(exercise => ({ name: exercise }))
          },

          update(store, { data }) {
            const newExercises = data.addExercises.exercises;

            const result = store.readQuery({
              query: queries.exercisesQuery,
              variables: {
                workoutId: workout.id
              }
            });

            result.exercises = [...newExercises, ...result.exercises];

            store.writeQuery({
              query: queries.exercisesQuery,
              variables: {
                workoutId: workout.id
              },
              data: result
            });
          }
        })
        .then(() => {
          showSnackbar("success", "Added exercises.");

          this.newExercises = [];
        })
        .catch(() => {
          this.newExercises = [];
          showSnackbar(
            "error",
            "Could not add exercises. Support has been notified."
          );
        });
    }
  },

  components: {
    AddCustomExercise
  },

  props: {
    workout: {
      type: Object,
      required: true
    }
  }
};
</script>
