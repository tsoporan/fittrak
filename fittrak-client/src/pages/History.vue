<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs12>
        <WorkoutHistoryToolbar />
        <WorkoutList />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import WorkoutList from "@/components/workouts/WorkoutList";
import WorkoutHistoryToolbar from "@/components/workouts/WorkoutHistoryToolbar";

export default {
  name: "History",
  components: {
    WorkoutList,
    WorkoutHistoryToolbar
  }
};
</script>

<style scoped>
</style>
