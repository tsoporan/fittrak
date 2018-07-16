<template>
  <div>
    <button v-on:click.prevent="removeExercise">Remove</button>
  </div>
</template>

<script>
import REMOVE_EXERCISE from "@/graphql/mutations/removeExercise.graphql";

export default {
  name: "RemoveExercise",

  methods: {
    removeExercise() {
      const { exercise } = this.$props;

      this.$apollo.mutate({
        mutation: REMOVE_EXERCISE,
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
