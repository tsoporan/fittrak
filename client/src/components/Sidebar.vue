<template>
<v-navigation-drawer app persistent clipped v-model="drawer">
  <v-list style="padding:0">
    <template v-for="item in items">
      <v-list-tile @click="$router.push(item.path)">
        <v-list-tile-action>
          <v-btn icon ripple>
            <v-icon color="grey">{{ item.icon }}</v-icon>
          </v-btn>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-title>{{ item. title }}</v-list-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-divider></v-divider>
    </template>
  </v-list>
</v-navigation-drawer>
</template>

<script>
import auth from '../auth'

export default {
  props: ['drawer'],
  data: () => ({
    items: [
      { id: 1, title: 'Home', icon: 'home', path: '/home' },
      { id: 2, title: 'Progress', icon: 'show_chart', path: '/progress' },
      { id: 3, title: 'History', icon: 'history', path: '/history' },
      { id: 4, title: 'Settings', icon: 'settings', path: '/settings' },
      { id: 5, title: 'Logout', icon: 'exit_to_app', path: '/logout' }
    ]
  }),
  methods: {
    logout () {
      return auth.logout()
    }
  }
}
</script>
