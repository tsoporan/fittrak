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
      @click.stop="addExercises"
      :disabled="!newExercises.length"
    >
    Add Exercises
    </v-btn>
  </v-form>
</template>

<script>
import ADD_EXERCISE from "@/graphql/mutations/addExercises.graphql";

export default {
  name: "AddExerciseForm",

  data: () => ({
    newExercises: [],
    exercises: ["Squat", "Bench Press"]
  }),

  methods: {
    addExercises() {
      const { workout } = this.$props;

      if (!this.newExercises.length) {
        return;
      }

      this.$apollo
        .mutate({
          mutation: ADD_EXERCISE,

          variables: {
            workoutId: workout.id,
            exercises: this.newExercises.map(exercise => ({ name: exercise }))
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
