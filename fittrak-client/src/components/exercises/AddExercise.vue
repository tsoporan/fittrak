<template>
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
  </v-form>
</template>

<script>
import ADD_EXERCISE from "@/graphql/mutations/addExercises.graphql";
import EXERCISE_TYPES from "@/graphql/queries/exerciseTypes.graphql";

export default {
  name: "AddExerciseForm",

  data: () => ({
    newExercises: [],
    exerciseTypes: []
  }),

  apollo: {
    exerciseTypes: {
      query: EXERCISE_TYPES,
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
