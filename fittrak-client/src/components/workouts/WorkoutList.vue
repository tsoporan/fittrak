<template>
  <div>
    <h2>{{ title }}</h2>
    <p v-if="activeWorkouts.length">
      <ul>
        <WorkoutItem
         v-for="workout in activeWorkouts"
          :key="workout.id"
          :workout="workout"
          />
      </ul>
    </p>
    <p v-else>
      No workouts!
    </p>
  </div>
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
      update: data => data.workouts
    }
  },

  computed: {
    activeWorkouts() {
      return this.workouts.filter(workout => workout.isActive);
    }
  },

  components: {
    WorkoutItem
  },

  props: {
    title: String
  }
};
</script>
