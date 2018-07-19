<template>
  <div>
    <ul class="workout-list" v-if="activeWorkouts.length">
      <WorkoutItem
        v-for="workout in activeWorkouts"
        :key="workout.id"
        :workout="workout"
        />
    </ul>
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
  }
};
</script>

<style scoped>
ul.workout-list {
  margin: 20px 0;
}
ul.workout-list li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
</style>
