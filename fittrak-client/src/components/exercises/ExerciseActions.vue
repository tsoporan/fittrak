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
    >
    </v-autocomplete>


    <v-btn
      @click.stop="addExercises"
      :disabled="!newExercises.length"
    >
    Add Exercises
    </v-btn>

    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-btn slot="activator" color="primary" dark>Add Custom</v-btn>
      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click.native="dialog = false">
            <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>Add Custom Exercise</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark flat @click.native="addCustomExercise">Save</v-btn>
          </v-toolbar-items>
        </v-toolbar>

        <v-card-text>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field placeholder="Exercise name" v-model="customExerciseName" />
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

  </v-form>
</v-flex>
</template>

<script>
import AddExercisesMutation from "@/graphql/mutations/addExercises.graphql";
import AddCustomExerciseMutation from "@/graphql/mutations/addCustomExercise.graphql";
import ExercisesQuery from "@/graphql/queries/exercises.graphql";
import ExerciseTypesQuery from "@/graphql/queries/exerciseTypes.graphql";
import MuscleGroupsQuery from "@/graphql/queries/muscleGroups.graphql";

import { EventBus } from "@/helpers";

export default {
  name: "AddExerciseForm",

  data: () => ({
    dialog: false,
    newExercises: [],
    exerciseTypes: [],
    muscleGroups: [],
    customMuscleGroupName: "",
    customExerciseName: ""
  }),

  apollo: {
    exerciseTypes: {
      query: ExerciseTypesQuery,
      update: data => data.exerciseTypes.map(exerciseType => exerciseType.name)
    },
    muscleGroups: {
      query: MuscleGroupsQuery,
      update: data => data.muscleGroups.map(group => group.name)
    }
  },

  methods: {
    addCustomExercise() {
      const { customMuscleGroupName, customExerciseName } = this;
      const { workout } = this.$props;

      if (!customMuscleGroupName.length || !customExerciseName.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: AddCustomExerciseMutation,

          variables: {
            workoutId: workout.id,
            exerciseName: customExerciseName,
            muscleGroupName: customMuscleGroupName
          },

          update(store, { data }) {
            const customExercise = data.addCustomExercise.exercise;

            const result = store.readQuery({
              query: ExercisesQuery,
              variables: {
                workoutId: workout.id
              }
            });

            result.exercises = [customExercise, ...result.exercises];

            store.writeQuery({
              query: ExercisesQuery,
              variables: {
                workoutId: workout.id
              },
              data: result
            });
          }
        })
        .then(() => {
          EventBus.$emit("show-snackbar", {
            type: "success",
            text: `Added exercise "${this.customExerciseName}".`
          });

          this.dialog = false;
          this.customMuscleGroupName = "";
          this.customExerciseName = "";
        })
        .catch(() => {
          EventBus.$emit("show-snackbar", {
            type: "error",
            text: "Could not add custom exercise. Support has been notified."
          });
        });
    },

    addExercises() {
      const { workout } = this.$props;

      if (!this.newExercises.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: AddExercisesMutation,

          variables: {
            workoutId: workout.id,
            exercises: this.newExercises.map(exercise => ({ name: exercise }))
          },

          update(store, { data }) {
            const newExercises = data.addExercises.exercises;

            const result = store.readQuery({
              query: ExercisesQuery,
              variables: {
                workoutId: workout.id
              }
            });

            result.exercises = [...newExercises, ...result.exercises];

            store.writeQuery({
              query: ExercisesQuery,
              variables: {
                workoutId: workout.id
              },
              data: result
            });
          }
        })
        .then(() => {
          EventBus.$emit("show-snackbar", {
            type: "success",
            text: "Added exercises."
          });

          this.newExercises = [];
        })
        .catch(() => {
          this.newExercises = [];
          EventBus.$emit("show-snackbar", {
            type: "error",
            text: "Could not add exercises. Support has been notified."
          });
        });
    }
  },

  props: {
    workout: Object
  }
};
</script>
