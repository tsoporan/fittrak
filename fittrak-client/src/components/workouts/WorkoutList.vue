<template>
  <v-flex 
    mt-5 
    v-if="$apollo.loading" 
    text-xs-center>
    <v-progress-circular 
      color="primary" 
      :indeterminate="true" 
      size="48"/>
  </v-flex>
  <v-flex v-else>
    <v-flex v-if="workouts.length">
      <v-list 
        two-line 
        subheader 
        class="mt-2">
        <v-subheader v-if="title">
          {{ title }}
        </v-subheader>
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
        const { status } = this.$props;

        const vars = {
          status
        };

        if (this.selectedStatus) {
          vars.status = this.selectedStatus;
        }

        return vars;
      },
      update(data) {
        const { limit } = this.$props;

        if (limit) return data.workouts.slice(0, limit);

        return data.workouts;
      }
    }
  },

  components: {
    WorkoutItem
  },

  props: {
    status: {
      type: String,
      required: false,
      default: ""
    },

    title: {
      type: String,
      required: true
    },

    limit: {
      type: Number,
      required: true
    }
  }
};
</script>

<style scoped>
</style>
