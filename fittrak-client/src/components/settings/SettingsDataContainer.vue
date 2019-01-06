<template>
  <v-layout 
    row 
    wrap>
    <slot :user="user"/>
  </v-layout>
</template>

<script>
import SettingsQuery from "@/graphql/queries/settings.graphql";

export default {
  name: "SettingsDataContainer",

  data() {
    return {
      user: {}
    };
  },

  apollo: {
    user: {
      query: SettingsQuery,
      update: data => data.viewer
    }
  }
};
</script>
