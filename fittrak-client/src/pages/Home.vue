<template>
  <v-container fluid fill-height grid-list-xl>
    <v-layout row align-center>
      <v-flex xs12 text-xs-center>
      <h2 class="display-2">
        It's {{ now.hourMin }} on {{ now.dayPart }} the {{ now.numPart }}.
        <br />
      </h2>

      <v-flex />

      <v-layout v-bind="layout" align-center>
        <v-flex xs6 text-xs-right><CreateWorkout /></v-flex>
        <v-flex xs1 text-xs-center>
          <v-card>
            <v-card-text>OR</v-card-text>
          </v-card>
        </v-flex>
        <v-flex xs6 text-xs-left><CreateWorkout /></v-flex>
      </v-layout>

      <v-layout>
        <v-flex xs-8>
          <WorkoutList :status="status" :limit=5 title="Recently" />
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

  data() {
    return {
      date: new Date()
    };
  },

  computed: {
    now: {
      get() {
        const date = this.date;

        if ("dayPart" in date) return date;

        const dayPart = format(date, "dddd");
        const numPart = format(date, "Mo");
        const hourMin = format(date, "h[:]mmA");

        return {
          dayPart,
          numPart,
          hourMin
        };
      },

      set(newDate) {
        this.date = newDate;
      }
    },

    status() {
      return PENDING;
    },

    layout() {
      // Allow dynamic layout opts based on screen size
      const layout = {};

      if (this.$vuetify.breakpoint.xs) {
        layout.column = true;
      }

      return layout;
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
