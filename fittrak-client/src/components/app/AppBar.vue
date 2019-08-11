<template>
  <div>
    <v-navigation-drawer v-model="drawer" app dark>
      <Sidebar :viewer="viewer" />
    </v-navigation-drawer>

    <v-app-bar color="primary" dark fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title
        class="logo"
        :class="{ main: $route.name === APP_NAME }"
        >{{ title }}</v-toolbar-title
      >
      <v-spacer />

      <slot></slot>
    </v-app-bar>
  </div>
</template>

<script>
import Sidebar from "@/components/app/Sidebar";

import { APP_NAME } from "@/constants";
import { queries } from "@/graphql";

export default {
  name: "AppBar",

  data() {
    return {
      drawer: null,
      viewer: { username: "..." },
      APP_NAME
    };
  },

  props: {
    title: {
      type: String,
      required: true
    }
  },

  components: {
    Sidebar
  },

  apollo: {
    viewer: {
      query: queries.viewerQuery,

      update(data) {
        return data.viewer;
      },

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
.logo.main {
  font-family: "Kaushan Script", "Roboto", "Arial";
  font-size: 32px;
}
.logo {
  font-family: "Roboto", "Arial";
  font-size: 24px;
}
</style>
