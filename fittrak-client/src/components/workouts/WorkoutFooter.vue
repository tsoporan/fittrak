<template>
  <v-footer app fixed dark color="grey lighten-2" height="64">
    <v-layout justify-center wrap justify-space-around>
      <slot></slot>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  name: "WorkoutFooter"
};
</script>
