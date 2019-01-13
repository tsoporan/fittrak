<template>
  <v-layout 
    row 
    wrap>
    <slot :user="user"/>
  </v-layout>
</template>

<script>
import ViewerQuery from "@/graphql/queries/viewer.graphql";

export default {
  name: "SettingsDataContainer",

  data() {
    return {
      user: {}
    };
  },

  apollo: {
    user: {
      query: ViewerQuery,
      update: data => data.viewer
    }
  }
};
</script>
