<template>
<v-snackbar
  v-model="open"
  :timeout="timeout"
  :bottom="bottom"
  :color="color"
>
  {{ text }}
  <v-btn
    flat
    @click="open = false"
  >
  Close
  </v-btn>
</v-snackbar>
</template>

<script>
export default {
  name: "ErrorSnackbar",

  data() {
    return {
      open: true,
      bottom: true,
      timeout: 7000,
      color: "error"
    };
  },

  props: {
    text: String
  }
};
</script>
