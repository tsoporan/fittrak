<template>
  <v-list three-line v-if="workouts.length">
    <WorkoutItem
      v-for="workout in workouts"
      :key="workout.id"
      :workout="workout"
      />
  </v-list>
  <p v-else> No workouts =( </p>
</template>

<script>
import WorkoutItem from "@/components/workouts/WorkoutItem";

import WORKOUTS from "@/graphql/queries/workouts.graphql";

export default {
  name: "WorkoutList",

  data() {
    return {
      workouts: []
    };
  },

  apollo: {
    workouts: {
      query: WORKOUTS,
      variables() {
        const { status } = this.$props;

        return {
          status
        };
      },
      update: data => data.workouts
    }
  },

  components: {
    WorkoutItem
  },

  props: {
    status: String
  }
};
</script>

<style scoped>
</style>
