<template>
  <li>
    ID: {{ set.id }}
    Weight: {{ set.weight }}
    Reps: {{ set.repetitions }}
    <hr />

    <RemoveSet :set=set />
  </li>
</template>

<script>
import RemoveSet from "@/components/sets/RemoveSet";

export default {
  name: "SetItem",

  components: {
    RemoveSet
  },

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
