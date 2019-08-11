<template>
  <v-card>
    <v-card-text> <slot name="icon">💡</slot> <slot></slot> </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Tip"
};
</script>
