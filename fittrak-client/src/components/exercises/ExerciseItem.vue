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

    <AddSet :exercise=exercise />
  </li>
</template>

<script>
import AddSet from "@/components/sets/AddSet";

export default {
  name: "ExerciseItem",
  props: {
    exercise: Object
  },
  components: {
    AddSet
  }
};
</script>

<style scoped>
li {
  border-bottom: 1px solid #ccc;
  padding: 10px;
}
</style>
