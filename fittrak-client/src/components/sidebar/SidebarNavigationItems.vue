<template>
<v-list dark>
  <router-link tag="v-list-tile" to="/">
    <v-list-tile-action>
      <v-icon>home</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>Home</v-list-tile-title>
    </v-list-tile-content>
  </router-link>

  <router-link tag="v-list-tile" to="/progress">
    <v-list-tile-action>
      <v-icon>trending_up</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>Progress</v-list-tile-title>
    </v-list-tile-content>
  </router-link>

  <router-link tag="v-list-tile" to="/history">
    <v-list-tile-action>
      <v-icon>history</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>History</v-list-tile-title>
    </v-list-tile-content>
  </router-link>

  <router-link tag="v-list-tile" to="/settings">
    <v-list-tile-action>
      <v-icon>settings</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>Settings</v-list-tile-title>
    </v-list-tile-content>
  </router-link>

  <v-divider />

  <v-list-tile @click="toReleaseNotes">
    <v-list-tile-action>
      <v-icon>notes</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>Release Notes</v-list-tile-title>
    </v-list-tile-content>
  </v-list-tile>

  <router-link tag="v-list-tile" to="/logout">
    <v-list-tile-action>
      <v-icon>exit_to_app</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title>Sign out</v-list-tile-title>
    </v-list-tile-content>
  </router-link>
</v-list>
</template>

<script>
export default {
  name: "SidebarNavigationItems",
  methods: {
    toReleaseNotes() {
      location.href = "https://github.com/tsoporan/fittrak/releases";
    }
  }
};
</script>
