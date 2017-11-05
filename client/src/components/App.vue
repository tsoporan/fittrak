<template>
<v-app>
  <Sidebar v-if="authed" v-bind:drawer="drawer"></Sidebar>

  <v-toolbar app clipped-left fixed color="cyan" dark flat>
    <v-toolbar-side-icon 
      app 
      v-if="authed" 
      @click.stop="drawer = !drawer"
    >
    </v-toolbar-side-icon> 

    <v-toolbar-title 
      color="white"
    >FitTrack</v-toolbar-title>

     <v-spacer></v-spacer>

    <v-toolbar-items v-if="!authed">
      <v-btn flat @click.prevent="$router.push('login')">Login</v-btn>
      <v-btn flat @click.prevent="$router.push('register')">Register</v-btn>
    </v-toolbar-items>
    <v-flex align-center v-else class="text-xs-right">
      Heya, <strong>{{username}}</strong>
    </v-flex>

  </v-toolbar>

  <main>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
          <router-view></router-view>
        </v-layout>
      </v-container>
    </v-content>
  </main>
  <v-footer app class="pa-2">
    <v-layout justify-center>
      Made with <span style="color:red;">&#10084;</span> by <a href="https://github.com/tsoporan/fittrack">tsoporan</a>
    </v-layout>
  </v-footer>
</v-app>
</template>

<script>
import Sidebar from './Sidebar'

import auth from '../auth'

export default {
  data: () => ({
    drawer: false
  }),
  computed: {
    authed () {
      return auth.user.authed
    },
    username () {
      return auth.user.username
    }
  },
  components: {
    Sidebar
  }
}
</script>
