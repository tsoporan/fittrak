<template>
<header>
  <h1>
    <router-link to="/">FitTrack</router-link>
  </h1>

  <div class="profile-menu">
      <div v-if="authed">
        <span class="username">Heya, <strong>{{ username }}</strong></span>
      </div>
      <div v-else>
        <router-link to="login" class="button is-secondary">Login</router-link>
        <router-link to="register" class="button is-secondary">Register</router-link>
      </div>
  </div>
</header>
</template>

<style lang="scss" scoped>
</style>

<script>
import auth from '../auth'

export default {
  methods: {
    toggleSidebar () {
      this.$store.dispatch('toggleSidebar')
    }
  },
  computed: {
    authed () {
      return auth.user.authed
    },
    username () {
      return auth.user.username
    }
  }
}
</script>

