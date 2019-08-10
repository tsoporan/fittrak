<template>
  <v-expansion-panels v-model="panel" :disabled="disabled" multiple>
    <v-expansion-panel v-for="exercise in exercises" :key="exercise.id">
      <v-expansion-panel-header>
        <span class="title">{{ exercise.name }}</span>
      </v-expansion-panel-header>

      <v-expansion-panel-content>
        <v-layout row wrap>
          <v-flex xs12>
            <v-btn
              small
              text
              color="info"
              icon
              @click.stop="removeExercise(exercise)"
            >
              <v-icon>delete</v-icon>
            </v-btn>
          </v-flex>

          <v-flex xs12>
            <h2 class="display-0">Add Set</h2>
            <AddSet :exercise="exercise" />
          </v-flex>

          <v-flex xs12>
            <h2 class="display-0">Set List</h2>
            <SetList :exercise="exercise" />
          </v-flex>
        </v-layout>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import { queries, mutations } from "@/graphql";

import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";

import { showSnackbar } from "@/helpers";

export default {
  name: "ExerciseList",

  data() {
    return {
      panel: [0],
      disabled: false
    };
  },

  methods: {
    removeExercise(exercise) {
      this.$apollo
        .mutate({
          mutation: mutations.RemoveExerciseMutation,
          variables: {
            exerciseId: exercise.id
          },
          update(store) {
            const result = store.readQuery({
              query: queries.ExercisesQuery,
              variables: {
                workoutId: exercise.workout.id
              }
            });

            result.exercises = result.exercises.filter(
              current => exercise.id !== current.id
            );

            store.writeQuery({
              query: queries.ExercisesQuery,
              variables: {
                workoutId: exercise.workout.id
              },
              data: result
            });
          }
        })
        .then(() => {
          showSnackbar("success", "Exercise removed.");
        })
        .error(() => {
          showSnackbar(
            "success",
            "Oops, could not remove exercise. Support has been notified."
          );
        });
    }
  },

  components: {
    AddSet,
    SetList
  },

  props: {
    exercises: {
      type: Array,
      required: true
    }
  }
};
</script>
