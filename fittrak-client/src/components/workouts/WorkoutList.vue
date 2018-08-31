<template>
  <v-flex mt-5 v-if="$apollo.loading" text-xs-center>
    <v-progress-circular color="primary" :indeterminate="true" size="48"></v-progress-circular>
  </v-flex>
  <v-flex v-else>
    <v-flex v-if="workouts.length">
      <v-flex v-if="title">
        <h3 class="headline">{{ title }}</h3>
      </v-flex>
      <v-list three-line class="mt-2">
        <WorkoutItem
          v-for="workout in workouts"
          :key="workout.id"
          :workout="workout"
          />
      </v-list>
    </v-flex>
    <v-flex v-else>
      <v-flex text-xs-center>No workouts available! 😞</v-flex>
    </v-flex>
  </v-flex>
</template>

<script>
import { getStatusBySlug } from "@/helpers";

import WorkoutItem from "@/components/workouts/WorkoutItem";

import WORKOUTS from "@/graphql/queries/workouts.graphql";

export default {
  name: "WorkoutList",

  data() {
    return {
      workouts: [],
      selectedStatus: null
    };
  },

  created() {
    // Set the status if we're currently in view
    const { status } = this.$route.params;

    if (status) {
      this.selectedStatus = getStatusBySlug(status);
    }
  },

  watch: {
    $route(to) {
      const { status } = to.params;

      if (status) {
        this.selectedStatus = getStatusBySlug(status);
      }
    }
  },

  apollo: {
    workouts: {
      query: WORKOUTS,
      variables() {
        const { status, limit } = this.$props;

        const vars = {
          status,
          limit
        };

        if (this.selectedStatus) {
          vars.status = this.selectedStatus;
        }

        return vars;
      },
      update: data => data.workouts
    }
  },

  components: {
    WorkoutItem
  },

  props: {
    status: String,
    title: String,
    limit: Number
  }
};
</script>

<style scoped>
</style>
