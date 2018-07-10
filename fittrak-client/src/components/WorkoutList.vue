<template>
  <div>
    <h2>{{ title }}</h2>
    <p v-if="workouts.length">
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

  components: {
    WorkoutItem
  },

  props: {
    title: String
  }
};
</script>
