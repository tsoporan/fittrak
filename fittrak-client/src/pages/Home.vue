<template>
  <v-container 
    fluid 
    fill-height 
    grid-list-xl>
    <v-layout 
      row 
      align-center>
      <v-flex 
        xs12 
        text-xs-center>
        <h2 class="display-2">
          It's {{ now.dayTime }} on {{ now.dayName }} the {{ now.dayNum }}.
          <br >
        </h2>

        <v-flex />

        <v-layout 
          v-bind="layout" 
          align-center>
          <CreateWorkout />
          <v-flex 
            xs1 
            text-xs-center>
            <v-flex>OR</v-flex>
          </v-flex>
          <v-flex 
            xs6 
            text-xs-left>
            <v-btn 
              large 
              disabled 
              @click.stop="" 
              class="success">
              Start Routine
            </v-btn>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-flex xs-8>
            <WorkoutList 
              :limit="limit" 
              title="Recently" />
          </v-flex>
        </v-layout>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import CreateWorkout from "@/components/workouts/CreateWorkout";
import WorkoutList from "@/components/workouts/WorkoutList";

import { PENDING, DEFAULT_LIMIT } from "@/constants";

import { format } from "date-fns";

export default {
  name: "Home",

  data() {
    return {
      date: new Date(),
      limit: DEFAULT_LIMIT
    };
  },

  computed: {
    now: {
      get() {
        const date = this.date;

        if ("dayPart" in date) return date;

        const dayName = format(date, "dddd");
        const dayNum = format(date, "Do");
        const dayTime = format(date, "h[:]mmA");

        return {
          dayName,
          dayNum,
          dayTime
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
