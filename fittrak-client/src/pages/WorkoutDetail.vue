<template>
  <v-container>
    <v-layout row wrap>

      <v-flex xs12>
        <v-layout justify-space-between>
          <v-flex xs2 text-xs-left>
            <v-btn flat color="secondary" outline>Back</v-btn>
          </v-flex>

          <v-flex xs2 text-xs-right>
            <StartWorkout :workout=workout v-if="pending" />
          </v-flex>
          <v-flex xs2 text-xs-right v-if="!complete && inProgress">
            <FinishWorkout :workout=workout />
          </v-flex>
            <!--
            <p class="control">
              <ReopenWorkout :workout=workout v-if="complete" />
            </p>
            -->
        </v-layout>
      </v-flex>

      <v-flex xs12>
        <AddExerciseForm :workout=workout v-if="!complete" />
      </v-flex>

      <v-flex xs12>
        <ExerciseList :workout=workout />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import WORKOUT from "@/graphql/queries/workout.graphql";

import AddExerciseForm from "@/components/exercises/AddExercise";
import ExerciseList from "@/components/exercises/ExerciseList";
import StartWorkout from "@/components/workouts/StartWorkout";
import FinishWorkout from "@/components/workouts/FinishWorkout";

import { COMPLETE, PENDING, IN_PROGRESS } from "@/constants";

export default {
  name: "WorkoutDetail",

  apollo: {
    workout: {
      query: WORKOUT,
      variables() {
        return {
          workoutId: this.$route.params.workoutId
        };
      },
      update: data => data.workout
    }
  },

  computed: {
    complete() {
      if (this.workout) {
        return this.workout.status === COMPLETE;
      }
    },
    pending() {
      if (this.workout) {
        return this.workout.status === PENDING;
      }
    },
    inProgress() {
      if (this.workout) {
        return this.workout.status === IN_PROGRESS;
      }
    }
  },

  components: {
    AddExerciseForm,
    ExerciseList,
    StartWorkout,
    FinishWorkout
  }
};
</script>

<style>
</style>
