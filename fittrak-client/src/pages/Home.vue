<template>
  <div class="page-content">
    <h2 class="page-header">Ongoing Workouts</h2>
    <hr />
    <CreateWorkout />
    <WorkoutList  />
  </div>
</template>

<script>
import CreateWorkout from "@/components/workouts/CreateWorkout.vue";
import WorkoutList from "@/components/workouts/WorkoutList.vue";

export default {
  name: "home",
  components: {
    CreateWorkout,
    WorkoutList
  }
};
</script>
