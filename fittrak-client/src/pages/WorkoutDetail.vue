<template>
  <div style="height:100%">
    <AppBar :title="title" />
    <v-container fill-height fluid v-if="$apollo.loading">
      <v-layout
        fill-height
        row
        align-center
        justify-center
        justify-content-center
      >
        <v-flex text-center>
          <Loader size="64" color="primary" />
          <p text-xs-center class="headline">
            🏋️ Loading workout ...
          </p>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container v-else fill-height fluid>
      <v-layout v-if="exercises.length">
        <ExerciseList :exercises="exercises" />
      </v-layout>
      <v-layout v-else fill-height row align-center justify-center>
        <p text-xs-center class="headline">
          Hrm, no exercises? 🤔
        </p>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { queries } from "@/graphql";

import Loader from "@/components/app/Loader";
import ExerciseList from "@/components/exercises/ExerciseList";
import AppBar from "@/components/app/AppBar";

export default {
  name: "Workout",

  data() {
    return {
      workout: {},
      exercises: [],
      title: `Workout #${this.$route.params.workoutId}`
    };
  },

  apollo: {
    workout: {
      query: queries.workoutQuery,
      variables() {
        const workoutId = this.$route.params.workoutId;

        return {
          workoutId
        };
      },
      update: data => data.workout
    },

    exercises: {
      query: queries.exercisesQuery,
      variables() {
        const workoutId = this.$route.params.workoutId;

        return {
          workoutId
        };
      },
      update: data => data.exercises
    }
  },

  components: {
    AppBar,
    ExerciseList,
    Loader
  }
};
</script>
