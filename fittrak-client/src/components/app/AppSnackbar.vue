<template>
  <v-snackbar v-model="open" :timeout="timeout" :bottom="bottom" :color="color">
    {{ text }}
    <v-btn dark text @click="open = false">
      Close
    </v-btn>
  </v-snackbar>
</template>

<script>
import { EventBus } from "@/helpers";

const DEFAULT_TIMEOUT = 7000;

export default {
  name: "AppSnackbar",

  created() {
    EventBus.$on("show-snackbar", msg => {
      this.open = true;
      this.color = msg.type;
      this.text = msg.text;
      this.timeout = msg.sticky ? 0 : msg.timeout || DEFAULT_TIMEOUT;
    });
  },

  data() {
    return {
      open: false,
      bottom: true,
      timeout: DEFAULT_TIMEOUT,
      color: "success", // Color matches type
      text: "",
      sticky: false
    };
  }
};
</script>
