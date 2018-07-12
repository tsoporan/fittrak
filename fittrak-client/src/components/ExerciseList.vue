<template>
  <div>
    <ul v-if="activeExercises.length">
      <ExerciseItem
        v-for="exercise in activeExercises"
        :key="exercise.id"
        :exercise="exercise"
      />
    </ul>
    <p v-else>
      No exercises!
    </p>
  </div>
</template>

<script>
import ExerciseItem from "./ExerciseItem";
import WORKOUT from "@/graphql/queries/workout.graphql";

export default {
  name: "ExerciseList",

  data() {
    return {
      workout: {
        exercises: []
      }
    };
  },

  apollo: {
    workout: {
      query: WORKOUT,
      variables() {
        return {
          workoutId: this.$route.params.workoutId
        };
      },
      update: data => data.viewer.workout
    }
  },

  computed: {
    activeExercises() {
      return this.workout.exercises.filter(e => e.isActive);
    }
  },

  components: {
    ExerciseItem
  }
};
</script>
