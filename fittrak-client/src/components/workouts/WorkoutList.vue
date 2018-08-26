<template>
  <div>
    <ul class="workout-list" v-if="workouts.length">
      <WorkoutItem
        v-for="workout in workouts"
        :key="workout.id"
        :workout="workout"
        />
    </ul>
    <p v-else>
      No available workouts!
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
ul.workout-list {
  margin: 20px 0;
}
ul.workout-list li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
</style>
