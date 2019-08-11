<template>
  <div>
    <v-list-item>
      <v-list-item-avatar size="32" color="grey darken-2">
        <v-icon>account_circle</v-icon>
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title
          >Heya,
          <span class="primary--text text--lighten-1">{{
            viewer.username
          }}</span></v-list-item-title
        >
      </v-list-item-content>
    </v-list-item>

    <v-divider />

    <v-list dense nav>
      <v-list-item link to="/" color="grey lighten-3">
        <v-list-item-icon>
          <v-icon>dashboard</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- TODO: Implement
      <v-list-item link to="/progress" color="grey lighten-3">
        <v-list-item-icon>
          <v-icon>trending_up</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Progress</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      -->

      <!-- TODO: Implement
      <v-list-item link to="/history" color="grey lighten-3">
        <v-list-item-icon>
          <v-icon>history</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>History</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      -->

      <v-list-item link to="/settings" color="grey lighten-3">
        <v-list-item-icon>
          <v-icon>settings</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider />

    <v-list dense nav>
      <v-list-item link @click="toReleaseNotes">
        <v-list-item-icon>
          <v-icon>notes</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Release Notes</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link @click="logout">
        <v-list-item-icon>
          <v-icon>exit_to_app</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Sign out</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
const RELEASES_URL = "https://github.com/tsoporan/fittrak/releases";
const LOGOUT_URL = "/accounts/logout/";

export default {
  name: "Sidebar",

  methods: {
    toReleaseNotes() {
      window.location.href = RELEASES_URL;
    },
    logout() {
      // Allow server side routing to kick in and logout session
      window.location.replace(LOGOUT_URL);
    }
  },

  props: {
    viewer: {
      type: Object,
      required: true
    }
  }
};
</script>
