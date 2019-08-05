<template>
  <v-layout row justify-space-around wrap mt-3 v-if="workouts.length">
    <template v-for="workout in coloredWorkouts">
      <v-flex xs12 md4 :key="workout.id">
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
import { getRandomColor } from "@/helpers";

import WorkoutCard from "@/components/workouts/WorkoutCard";
import WorkoutFilterToolbar from "@/components/workouts/WorkoutFilterToolbar";

export default {
  name: "WorkoutCardList",

  data() {
    return {
      selectedStatus: null
    };
  },

  computed: {
    coloredWorkouts() {
      return this.workouts.map(workout => ({
        ...workout,
        color: getRandomColor()
      }));
    }
  },

  components: {
    WorkoutCard,
    WorkoutFilterToolbar
  },

  props: {
    workouts: {
      type: Array,
      required: true
    }
  }
};
</script>
