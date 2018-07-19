<template>
  <form>
    <div class="field has-addons">
      <p class="control">
      <input class="input" v-model="exerciseName" type="text" placeholder="Exercise name ...">
      </p>
      <p class="control">
      <button class="button is-primary is-outlined" v-on:click.prevent="addExercise">Add Exercise</button>
      </p>
    </div>
  </form>
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
