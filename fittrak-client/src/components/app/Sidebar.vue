<template>
  <div>
    <v-list-item>
      <v-list-item-avatar size="32">
        <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
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

    <v-list dense nav flat>
      <v-list-item link to="/">
        <v-list-item-icon>
          <v-icon>home</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link to="/progress">
        <v-list-item-icon>
          <v-icon>trending_up</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Progress</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link to="/history">
        <v-list-item-icon>
          <v-icon>history</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>History</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link to="/settings">
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
export default {
  name: "SidebarNavigationItems",

  methods: {
    toReleaseNotes() {
      window.location.href = "https://github.com/tsoporan/fittrak/releases";
    },
    logout() {
      // Allow server side routing to kick in and logout session
      window.location.replace("/accounts/logout/");
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
