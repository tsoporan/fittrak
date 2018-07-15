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
import ExerciseItem from "@/components/exercises/ExerciseItem";

export default {
  name: "ExerciseList",

  computed: {
    activeExercises() {
      const { workout } = this.$props;

      if (!workout) return [];

      return workout.exercises.filter(e => e.isActive);
    }
  },

  components: {
    ExerciseItem
  },

  props: {
    workout: Object
  }
};
</script>
