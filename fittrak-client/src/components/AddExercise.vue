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
      const workoutId = parseInt(this.$route.params.workoutId, 10);

      this.$apollo
        .mutate({
          mutation: ADD_EXERCISE,
          variables: {
            workoutId: workoutId,
            exerciseName: this.exerciseName
          }
        })
        .then(resp => {
          console.log("*** resp", resp);
        })
        .catch(err => {
          console.error("** err", err);
        });
    }
  },
  props: {
    workoutId: String
  }
};
</script>
