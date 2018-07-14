<template>
  <div>
    <h2>Workout Detail</h2>
    <AddExercise />
    <ExerciseList />
  </div>
</template>

<script>
import AddExercise from "@/components/exercises/AddExercise";
import ExerciseList from "@/components/exercises/ExerciseList";

export default {
  name: "WorkoutDetail",
  components: {
    AddExercise,
    ExerciseList
  }
};
</script>
