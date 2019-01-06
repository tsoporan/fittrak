<template>
  <v-flex xs12>
    Test
    {{ user.id }}
  </v-flex>
</template>

<script>
export default {
  name: "UserSettings",

  props: {
    user: {
      type: Object,
      required: true
    }
  }
};
</script>
