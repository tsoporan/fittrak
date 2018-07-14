<template>
  <div>
    <WorkoutList title="Current Workouts" />
    <CreateWorkout />
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
