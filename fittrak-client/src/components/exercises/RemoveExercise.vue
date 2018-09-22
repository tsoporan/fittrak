<template>
  <button class="button" v-on:click.prevent="removeExercise">Remove Exercise</button>
</template>

<script>
import RemoveExerciseQuery from "@/graphql/mutations/removeExercise.graphql";
import ExercisesQuery from "@/graphql/queries/exercises.graphql";

export default {
  name: "RemoveExercise",

  methods: {
    removeExercise() {
      const { exercise } = this.$props;

      this.$apollo.mutate({
        mutation: RemoveExerciseQuery,
        variables: {
          exerciseId: exercise.id
        }
      });
    }
  },

  props: {
    exercise: Object
  }
};
</script>
