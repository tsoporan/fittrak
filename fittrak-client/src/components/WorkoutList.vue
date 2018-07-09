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
  data() {
    return {
      workouts: []
    };
  },

  apollo: {
    workouts: {
      query() {
        return gql`
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
        `;
      },

      update: data => data.viewer.workouts
    }
  }
};
</script>
