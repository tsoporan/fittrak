<template>
<v-app id="fittrak">
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
      <v-progress-circular size="24" :indeterminate="true" v-if="$apollo.loading"></v-progress-circular>
      <v-flex v-else>Heya, <strong>{{ viewer }}</strong></v-flex>
    </v-flex>
  </v-toolbar>

  <v-content>
    <router-view />
  </v-content>
</v-app>
</template>

<script>
import VIEWER from "@/graphql/queries/viewer.graphql";

import SidebarNavigationItems from "@/components/sidebar/SidebarNavigationItems";

export default {
  name: "App",

  data: () => ({
    drawer: null,
    viewer: "Stranger"
  }),

  props: {
    source: String
  },

  components: {
    SidebarNavigationItems
  },

  apollo: {
    viewer: {
      query: VIEWER,
      update: data => data.viewer.username
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
