<template>
  <v-progress-circular :color="color" :size="size" :indeterminate="true" />
</template>

<script>
export default {
  name: "Loader",

  props: {
    color: {
      type: String,
      required: false,
      default: "white"
    },
    size: {
      type: String,
      required: false,
      default: "24"
    }
  }
};
</script>
