<template>
  <li>
    <h2>Exercise Details</h2>
    <div>
      <p>ID: #{{ exercise.id }}</p>
      <p>Name: {{ exercise.name }}</p>
      <p>Started: {{ exercise.dateStarted }}</p>
      <br />
      <RemoveExercise :exercise=exercise />
    </div>

    <hr />

    <h2> Add Set </h2>
    <AddSet :exercise=exercise />

    <hr />

    <h2>Set List</h2>
    <SetList :exercise=exercise />
  </li>
</template>

<script>
import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";
import RemoveExercise from "@/components/exercises/RemoveExercise";

export default {
  name: "ExerciseItem",

  components: {
    AddSet,
    SetList,
    RemoveExercise
  },

  props: {
    exercise: Object
  }
};
</script>

<style scoped>
li {
  border-bottom: 1px solid #ddd;
  padding: 10px;
}
</style>
