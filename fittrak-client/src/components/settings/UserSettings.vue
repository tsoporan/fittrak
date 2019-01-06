<template>
  <v-flex xs12>
    {{ user.id }}
    {{ user.email }}
    {{ user.username }}
    {{ user.profile.preferredUnit }}
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
