<template>
  <v-form class="ma-4">
    <v-autocomplete
      v-model="newExercises"
      :items="exercises"
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
      @click.stop="addExercise"
      :disabled="!newExercises.length"
    >
    Add Exercises
    </v-btn>
  </v-form>
</template>

<script>
import ADD_EXERCISE from "@/graphql/mutations/addExercise.graphql";

export default {
  name: "AddExerciseForm",

  data: () => ({
    newExercises: [],
    exercises: ["Squat", "Bench Press"]
  }),

  methods: {
    addExercise() {
      const { workout } = this.$props;

      if (!this.newExercises.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: ADD_EXERCISE,

          variables: {
            workoutId: workout.id,
            exerciseName: this.exerciseName
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
