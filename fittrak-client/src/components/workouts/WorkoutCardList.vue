<template>
  <v-layout row wrap mt-3 v-if="workouts.length">
    <template v-for="workout in mappedWorkouts">
      <v-flex xs12 md3 :key="workout.id">
        <WorkoutCard :workout="workout" :key="workout.id" />
      </v-flex>
    </template>
  </v-layout>

  <v-layout v-else text-xs-center align-content-center>
    <v-flex>
      <span class="headline">
        No workouts available! 😞
      </span>
    </v-flex>
  </v-layout>
</template>

<script>
import { getStatusColor } from "@/helpers";

import WorkoutCard from "@/components/workouts/WorkoutCard";

export default {
  name: "WorkoutCardList",

  data() {
    return {
      selectedStatus: null
    };
  },

  computed: {
    mappedWorkouts() {
      return this.workouts.map(workout => ({
        ...workout,
        color: getStatusColor(workout.status)
      }));
    }
  },

  components: {
    WorkoutCard
  },

  props: {
    workouts: {
      type: Array,
      required: true
    }
  }
};
</script>
