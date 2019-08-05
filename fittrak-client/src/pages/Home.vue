<template>
  <div>
    <AppBar title="FitTrak">
      <v-btn>Test</v-btn>
    </AppBar>

    <v-container fluid>
      <v-layout row pa-4>
        <WorkoutFilterToolbar />
      </v-layout>
      <v-layout row fill-height pa-4 justify-center>
        <Loader color="primary" size="64" v-if="$apollo.loading" />
        <v-container grid-list-xl fluid v-else>
          <WorkoutCardList :workouts="workouts" />
        </v-container>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { queries } from "@/graphql";

import AppBar from "@/components/app/AppBar";
import Loader from "@/components/app/Loader";
import WorkoutFilterToolbar from "@/components/workouts/WorkoutFilterToolbar";
import WorkoutCardList from "@/components/workouts/WorkoutCardList";

import { showSnackbar } from "@/helpers";

export default {
  name: "Home",

  data() {
    return {
      workouts: []
    };
  },

  apollo: {
    workouts: {
      query: queries.workoutsQuery,

      update(data) {
        return data.workouts;
      },

      error() {
        showSnackbar("error", "Could not load workouts.");
      }
    }
  },

  components: {
    AppBar,
    WorkoutFilterToolbar,
    WorkoutCardList,
    Loader
  }
};
</script>
