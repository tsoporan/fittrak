<template>
  <v-container>
    <v-layout row>
      <UserSettings :viewer="viewer" />
    </v-layout>
  </v-container>
</template>

<script>
import { queries } from "@/graphql";

import UserSettings from "@/components/settings/UserSettings";

export default {
  name: "SettingsPage",

  data() {
    return {
      viewer: {}
    };
  },

  apollo: {
    viewer: {
      query: queries.viewerQuery
    },

    update(data) {
      return data.viewer;
    }
  },

  components: {
    UserSettings
  }
};
</script>
