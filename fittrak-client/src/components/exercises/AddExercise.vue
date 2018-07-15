<template>
  <div>
    <form>
      <input v-model="exerciseName" type="text" placeholder="Exercise name ...">
      <button v-on:click.prevent="addExercise">Add Exercise</button>
    </form>
  </div>
</template>

<script>
import ADD_EXERCISE from "@/graphql/mutations/addExercise.graphql";

export default {
  name: "AddExercise",

  data() {
    return {
      exerciseName: ""
    };
  },

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
    }
  },

  props: {
    workout: Object
  }
};
</script>
