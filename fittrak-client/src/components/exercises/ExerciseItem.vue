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
  </li>
</template>

<script>
import AddSet from "@/components/sets/AddSet";
import SetList from "@/components/sets/SetList";

export default {
  name: "ExerciseItem",
  props: {
    exercise: Object
  },
  components: {
    AddSet,
    SetList
  }
};
</script>

<style scoped>
li {
  border-bottom: 1px solid #ccc;
  padding: 10px;
}
</style>
