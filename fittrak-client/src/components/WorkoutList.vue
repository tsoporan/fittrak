<template>
  <div>
    <h2>{{ title }}</h2>
    <p v-if="activeWorkouts.length">
      <ul>
        <WorkoutItem
         v-for="workout in workouts"
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
import WorkoutItem from "./WorkoutItem";

import VIEWER_WORKOUTS from "@/graphql/queries/viewerWorkouts.graphql";

export default {
  name: "WorkoutList",

  data() {
    return {
      workouts: []
    };
  },

  apollo: {
    workouts: {
      query: VIEWER_WORKOUTS,
      update: data => data.viewer.workouts
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
