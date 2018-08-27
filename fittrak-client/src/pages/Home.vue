<template>
  <v-container fluid fill-height grid-list-xl>
    <v-layout row align-center>
    <v-flex xs12>
        <h2 class="display-2">
          It's {{ now.hourMin }} on {{ now.dayPart }} the {{ now.numPart }}.
          Let's get started!
        </h2>

        <v-flex />

        <v-layout row>
          <v-flex xs6 text-xs-center><CreateWorkout /></v-flex>
          <v-flex xs6 text-xs-center><CreateWorkout /></v-flex>
        </v-layout>
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import CreateWorkout from "@/components/workouts/CreateWorkout.vue";
import WorkoutList from "@/components/workouts/WorkoutList.vue";

import { PENDING } from "@/constants";

import { format } from "date-fns";

export default {
  name: "home",
  computed: {
    now() {
      const date = new Date();

      const dayPart = format(date, "dddd");
      const numPart = format(date, "Mo");
      const hourMin = format(date, "h[:]mmA");

      return {
        dayPart,
        numPart,
        hourMin
      };
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

<style scoped>
</style>
