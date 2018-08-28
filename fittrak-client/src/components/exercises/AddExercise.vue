<template>
  <v-form class="ma-4">
    <v-text-field
      v-model="exerciseName"
      required
      placeholder="Exercise name"
    >
    </v-text-field>

    <v-btn
      @click.stop="addExercise"
      :disabled="!isValidName()"
    >
    Add Exercise
    </v-btn>
  </v-form>
</template>

<script>
import ADD_EXERCISE from "@/graphql/mutations/addExercise.graphql";

export default {
  name: "AddExerciseForm",

  data: () => ({
    exerciseName: ""
  }),

  methods: {
    addExercise() {
      const { workout } = this.$props;

      if (!this.exerciseName) {
        return;
      }

      this.$apollo.mutate({
        mutation: ADD_EXERCISE,

        variables: {
          workoutId: workout.id,
          exerciseName: this.exerciseName
        }
      });
    },

    isValidName() {
      const name = this.exerciseName;

      return name.trim().length > 0;
    }
  },

  props: {
    workout: Object
  }
};
</script>
