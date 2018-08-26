<template>
  <div class="page-content">
    <h1 class="title">It's {{ now }}, time to get crackin'!</h1>

    <h2 class="page-header">Ongoing Workouts</h2>

    <hr />
    <CreateWorkout />
    <WorkoutList :status="status" />
  </div>
</template>

<script>
import CreateWorkout from "@/components/workouts/CreateWorkout.vue";
import WorkoutList from "@/components/workouts/WorkoutList.vue";

import { PENDING } from "@/constants";

export default {
  name: "home",
  computed: {
    now() {
      return new Date().toString();
    },
    status() {
      return PENDING;
    }
  },
  components: {
    CreateWorkout,
    WorkoutList
  }
};
</script>
