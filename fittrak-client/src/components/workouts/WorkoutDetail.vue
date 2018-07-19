<template>
  <div>
    <h2>Workout Detail</h2>

    <header id="workout-header">
      <AddExercise :workout=workout />
      <StartWorkout :workout=workout v-if="pending" />
      <FinishWorkout :workout=workout v-if="!complete" />
    </header>

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

import { COMPLETE, PENDING} from "@/components/constants";

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
