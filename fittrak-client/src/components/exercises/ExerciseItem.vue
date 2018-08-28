<template>
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

<style>
</style>
