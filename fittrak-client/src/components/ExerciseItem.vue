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
  </li>
</template>

<script>
export default {
  name: "ExerciseItem",
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
