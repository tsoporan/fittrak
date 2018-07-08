<template>
  <div>
    <h2>Workouts</h2>
    <p v-if="workouts">
      Workouts
    </p>
    <p v-else>
      No workouts!
    </p>
  </div>
</template>

<script>
import gql from "graphql-tag";

export default {
  apollo: {
    workouts: gql`
      {
        viewer {
          workouts {
            id
            dateStarted
            dateEnded
            isActive
          }
        }
      }
    `
  }
};
</script>
