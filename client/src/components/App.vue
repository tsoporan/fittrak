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
      style="font-family: Kaushan Script; font-size: 24px"
    >
    FitTrack
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-toolbar-items v-if="!authed">
      <v-btn flat @click.prevent="$router.push('/signin')">Sign In</v-btn>
      <v-btn flat @click.prevent="$router.push('/register')">Register</v-btn>
    </v-toolbar-items>
    <v-flex align-center v-else class="text-xs-right">
      Heya, <strong>{{ username }}</strong>
    </v-flex>

  </v-toolbar>

  <main>
    <v-content>
      <template v-if="authed && !initialFetch">
        <v-container fluid fill-height>
          <Loader></Loader>
        </v-container>
      </template>
      <template v-else>
      <v-container fluid fill-height>
        <router-view></router-view>
      </v-container>
      </template>
    </v-content>
  </main>

  <Footer></Footer>
  </v-app>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

import Sidebar from './Sidebar'
import Footer from './Footer'
import Loader from './Loader'

export default {
  data: () => ({
    drawer: false
  }),
  computed: {
    ...mapState({
      authed: state => state.user.authed,
      username: state => state.user.username
    }),
    ...mapGetters(['initialFetch'])
  },
  components: {
    Sidebar,
    Footer,
    Loader
  }
}
</script>
