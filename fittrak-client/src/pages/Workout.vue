<template>
  <v-container
    fill-height
    v-if="$apollo.loading"
  >
    <v-layout 
      row
      wrap
      align-center
      justify-center
    >
      <v-flex text-xs-center>
        <Loader 
          size="48"
          color="primary"
        />
        <span class="headline">
          Preparing workout ...
        </span>
      </v-flex>
    </v-layout>
  </v-container>
  <v-container
    row 
    wrap
    v-else
  >
    <v-layout 
      row 
      wrap>
      <WorkoutHeader :workout="workout" />
      <ExerciseActions :workout="workout" />
      <ExerciseList :exercises="exercises" />
    </v-layout>
  </v-container>
</template>

<script>
import { queries } from "@/graphql";

import Loader from "@/components/app/Loader";
import WorkoutHeader from "@/components/workouts/WorkoutHeader";
import ExerciseActions from "@/components/exercises/ExerciseActions";
import ExerciseList from "@/components/exercises/ExerciseList";

export default {
  name: "Workout",

  data() {
    return {
      workout: {},
      exercises: []
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
    WorkoutHeader,
    ExerciseActions,
    ExerciseList,
    Loader
  }
};
</script>
