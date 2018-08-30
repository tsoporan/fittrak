<template>
  <v-flex mt-5 v-if="$apollo.loading">
    <v-progress-circular color="primary" :indeterminate="true" size="48"></v-progress-circular>
  </v-flex>
  <v-flex v-else>
    <v-flex v-if="workouts.length">
      <h3 class="display-1">{{ title }}</h3>
      <v-divider />
      <v-list three-line>
        <WorkoutItem
          v-for="workout in workouts"
          :key="workout.id"
          :workout="workout"
          />
      </v-list>
    </v-flex>
    <v-flex v-else>
      <v-card>No recent workouts! Add one above to get started! 💪</v-card></v-flex>
  </v-flex>
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
    status: String,
    title: String
  }
};
</script>

<style scoped>
</style>
