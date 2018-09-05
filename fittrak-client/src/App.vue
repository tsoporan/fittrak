<template>
<v-app id="fittrak" v-if="!$apollo.loading && !error">
  <v-navigation-drawer
    v-model="drawer"
    fixed
    app
    dark
  >
    <SidebarNavigationItems  />
  </v-navigation-drawer>

  <v-toolbar color="primary" dark fixed app>
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-toolbar-title class="logo">FitTrak</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-flex text-xs-right>
      <v-flex>Heya, <strong>{{ viewer }}</strong></v-flex>
    </v-flex>
  </v-toolbar>

  <v-content>
    <router-view />
  </v-content>
</v-app>
<v-app v-else>
  <v-layout justify-center align-center fill-height>
    <v-flex text-xs-center>
      <v-progress-circular color="primary" size="64" :indeterminate="true"></v-progress-circular>
      <v-flex mt-2>Firing up ... 💪</v-flex>
      <v-flex v-if="error" mt-2>
        <p>
          Hmm, looks like there was an issue making the connection. Please try again!
          If this persists please contact: <a href="mailto:help@fittrak.ca">help@fittrak.ca</a>
        </p>
        <v-btn @click="signOut" depressed color="secondary">Sign out</v-btn>
      </v-flex>
    </v-flex>
  </v-layout>
</v-app>
</template>

<script>
import VIEWER from "@/graphql/queries/viewer.graphql";

import SidebarNavigationItems from "@/components/sidebar/SidebarNavigationItems";

import { SIGNOUT_URL } from "@/constants";

export default {
  name: "App",

  data: () => ({
    drawer: null,
    viewer: "Stranger",
    error: false
  }),

  methods: {
    signOut() {
      this.$router.replace(SIGNOUT_URL);
    }
  },

  props: {
    source: String
  },

  components: {
    SidebarNavigationItems
  },

  apollo: {
    viewer: {
      query: VIEWER,
      update: data => data.viewer.username,
      error(error) {
        // TODO: Send error up
        console.log(`Error: ${error}`); // eslint-disable-line
        this.error = true;
      }
    }
  }
};
</script>

<style>
.logo {
  font-family: "Kaushan Script", "Roboto", "Arial";
  font-size: 32px;
}
</style>
