<template>
  <div>
    <WorkoutList title="Current Workouts" />
    <CreateWorkout />
  </div>
</template>

<script>
import CreateWorkout from "@/components/CreateWorkout.vue";
import WorkoutList from "@/components/WorkoutList.vue";

export default {
  name: "home",
  components: {
    CreateWorkout,
    WorkoutList
  }
};
</script>
