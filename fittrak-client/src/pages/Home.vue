<template>
  <div>
    <AppBar title="FitTrak">
      <v-btn>Test</v-btn>
    </AppBar>
    <v-container fluid grid-list-xl>
      <v-layout row>
        <v-flex>
          <WorkoutFilterHeader />
        </v-flex>
      </v-layout>
      <v-layout fill-height>
        <v-flex v-if="$apollo.loading">
          <Loader color="primary" size="48" />
        </v-flex>
        <v-flex v-else>
          <WorkoutCardList :workouts="workouts" />
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { queries } from "@/graphql";

import AppBar from "@/components/app/AppBar";
import Loader from "@/components/app/Loader";
import WorkoutFilterHeader from "@/components/workouts/WorkoutFilterHeader";
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
    WorkoutFilterHeader,
    WorkoutCardList,
    Loader
  }
};
</script>
