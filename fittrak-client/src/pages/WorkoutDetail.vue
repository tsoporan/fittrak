<template>
  <div class="page-content">
    <h2 class="page-header">Workout Details</h2>
    <hr />

    <div class="field is-grouped">
      <p class="control">
        <AddExercise :workout=workout v-if="!complete" />
      </p>
      <p class="control">
        <StartWorkout :workout=workout v-if="pending" />
      </p>
      <p class="control">
        <FinishWorkout :workout=workout v-if="!complete && inProgress" />
      </p>
      <!--
      <p class="control">
        <ReopenWorkout :workout=workout v-if="complete" />
      </p>
      -->
    </div>

    <div id="exercises">
      <ExerciseList :workout=workout />
    </div>
  </div>
</template>

<script>
import WORKOUT from "@/graphql/queries/workout.graphql";

import AddExercise from "@/components/exercises/AddExercise";
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
    AddExercise,
    ExerciseList,
    StartWorkout,
    FinishWorkout
  }
};
</script>

<style>
#exercises {
  margin: 20px;
}

#workout-header form {
  padding: 10px;
  margin: 5px 0;
}
</style>
