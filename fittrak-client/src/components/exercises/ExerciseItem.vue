<template>
  <li>
    <div>
    ID: {{ exercise.id }}
    </div>

    <div>
    Name: {{ exercise.name }}
    </div>

    <div>
    Started: {{ exercise.dateStarted }}
    </div>

    <hr />

    <AddSet :exercise=exercise />
    <SetList :exercise=exercise />

    <hr />
    <RemoveExercise :exercise=exercise />
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
  border-bottom: 1px solid #ccc;
  padding: 10px;
}
</style>
