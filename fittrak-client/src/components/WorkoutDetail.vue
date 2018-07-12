<template>
  <div>
    <h2>Workout Detail</h2>
    <AddExercise />
    <ExerciseList />
  </div>
</template>

<script>
import AddExercise from "./AddExercise";
import ExerciseList from "./ExerciseList";

export default {
  name: "WorkoutDetail",
  components: {
    AddExercise,
    ExerciseList
  }
};
</script>
