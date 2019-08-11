<template>
  <v-dialog
    v-model="dialog"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <v-btn slot="activator" color="primary" dark>Add Custom</v-btn>
    <v-card>
      <v-toolbar dark color="primary">
        <v-btn icon dark @click.native="dialog = false">
          <v-icon>close</v-icon>
        </v-btn>
        <v-toolbar-title>Add Custom Exercise</v-toolbar-title>
        <v-spacer />
        <v-toolbar-items>
          <v-btn dark flat @click.native="addCustomExercise">Save</v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-card-text>
        <v-layout wrap>
          <v-flex xs12>
            <v-text-field
              placeholder="Exercise name"
              v-model="customExerciseName"
            />
          </v-flex>

          <v-flex xs12>
            <v-autocomplete
              v-model="customMuscleGroupName"
              :items="muscleGroups"
              placeholder="Select muscle group"
              browser-autocomplete
              clearable
            />
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import { queries, mutations } from "@/graphql";

import { showSnackbar } from "@/helpers";

export default {
  name: "AddCustomExercise",

  data() {
    return {
      dialog: false,
      customMuscleGroupName: "",
      customExerciseName: "",
      muscleGroups: []
    };
  },

  apollo: {
    muscleGroups: {
      query: queries.muscleGroupsQuery,
      update: data => data.muscleGroups.map(group => group.name)
    }
  },

  methods: {
    addCustomExercise() {
      const { customMuscleGroupName, customExerciseName } = this;
      const workout = this.workout;

      if (!customMuscleGroupName.length || !customExerciseName.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: mutations.addCustomExerciseMutation,

          variables: {
            workoutId: workout.id,
            exerciseName: customExerciseName,
            muscleGroupName: customMuscleGroupName
          },

          update(store, { data }) {
            const customExercise = data.addCustomExercise.exercise;

            const result = store.readQuery({
              query: queries.exercisesQuery,
              variables: {
                workoutId: workout.id
              }
            });

            result.exercises = [customExercise, ...result.exercises];

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
          showSnackbar(
            "success",
            `Added new exercise "${this.customExerciseName}".`
          );

          this.dialog = false;
          this.customMuscleGroupName = "";
          this.customExerciseName = "";
        })
        .catch(() => {
          showSnackbar(
            "error",
            "Could not add custom exercise. Support has been notified."
          );
        });
    }
  },

  props: {
    workout: {
      type: Object,
      required: true
    }
  }
};
</script>
