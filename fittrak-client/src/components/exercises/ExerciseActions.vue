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
          <v-toolbar-title>Settings</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark flat @click.native="dialog = false">Save</v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </v-card>
    </v-dialog>

  </v-form>
</v-flex>
</template>

<script>
import AddExerciseMutation from "@/graphql/mutations/addExercises.graphql";
import ExercisesQuery from "@/graphql/queries/exercises.graphql";
import ExerciseTypesQuery from "@/graphql/queries/exerciseTypes.graphql";

export default {
  name: "AddExerciseForm",

  data: () => ({
    dialog: false,
    newExercises: [],
    exerciseTypes: []
  }),

  apollo: {
    exerciseTypes: {
      query: ExerciseTypesQuery,
      update: data => data.exerciseTypes.map(exerciseType => exerciseType.name)
    }
  },

  methods: {
    addExercises() {
      const { workout } = this.$props;

      if (!this.newExercises.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: AddExerciseMutation,

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
          this.newExercises = [];
        });
    }
  },

  props: {
    workout: Object
  }
};
</script>
