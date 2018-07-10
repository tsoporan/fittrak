<template>
  <div>
    <button v-on:click="createWorkout">Create New Workout</button>
  </div>
</template>

<script>
import gql from "graphql-tag";

import CREATE_WORKOUT from "../graphql/createWorkout.gql";

export default {
  name: "CreateWorkout",

  methods: {
    createWorkout() {
      console.log("creating workout");

      this.$apollo.mutate({
        mutation: CREATE_WORKOUT,

        update: (store, { data }) => {
          console.log("*** store", store);
          const workout = data.createWorkout.workout;
          console.log("**** workout", workout);
        }
      });
    }
  }
};
</script>
