<template>
  <li>
    ID: {{ set.id }}
    Weight: {{ set.weight }}
    Reps: {{ set.repetitions }}
  </li>
</template>

<script>
export default {
  name: "SetItem",
  props: {
    set: Object
  }
};
</script>

<style scoped>
li {
  margin: 10px;
}
</style>
