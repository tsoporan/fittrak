<template>
  <v-container fluid fill-height grid-list-xl>
    <v-layout row align-center>
      <v-flex xs12 text-xs-center>
      <h2 class="display-2">
        It's {{ now.hourMin }} on {{ now.dayPart }} the {{ now.numPart }}.
        <br />
      </h2>

      <v-flex />

      <v-layout row>
        <v-flex xs6 text-xs-right><CreateWorkout /></v-flex>
        <v-flex xs1></v-flex>
        <v-flex xs6 text-xs-left><CreateWorkout /></v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs-8>
          <h3 class="display-1">Recently</h3>
          <WorkoutList :status="status" :limit=5 />
        </v-flex>
      </v-layout>
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import CreateWorkout from "@/components/workouts/CreateWorkout";
import WorkoutList from "@/components/workouts/WorkoutList";

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
