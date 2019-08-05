<template>
  <div>
    <AppBar title="Settings" />
    <v-container>
      <v-layout row>
        <UserSettings :viewer="viewer" />
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { queries } from "@/graphql";

import AppBar from "@/components/app/AppBar";
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
    AppBar,
    UserSettings
  }
};
</script>
