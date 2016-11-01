<template>
<header>
<div class="columns is-mobile">
    <div class="column is-half">
    <h1>
      <button>
        <span class="icon is-medium" v-on:click="toggleSidebar"> <i class="fa fa-bars"></i> </span>
      </button>
      <router-link to="/">FitTrack</router-link>
    </h1>
    </div>

    <div class="column">
    <div class="profile-menu">
        <div v-if="isAuthed">
          Hi, {{ username }}
          <a href="" @click.prevent="logout">Logout</a>
        </div>
        <div v-else>
          <router-link to="login" class="button is-secondary">Login</router-link>
          <router-link to="register" class="button is-secondary">Register</router-link>
        </div>
    </div>
    </div>
</div>
</header>
</template>

<style lang="scss" scoped>
$white: #ffffff;
$darkgrey: #4a4a4a;

header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  background: $white;
  padding: .1rem;
}

header h1 {
  font-family: 'Kaushan Script', cursive;
  padding: 0;
}

header h1 a {
  display: inline-block;
  vertical-align: middle;
  font-size: 2rem;
}

header h1 button {
  color: $darkgrey;
  display: inline-block;
  vertical-align: middle;
  border: none;
  background: #fff;
}

div.profile-menu {
  text-align: right;
  margin-right: 1rem;
  margin-top: .3rem;
}

</style>

<script>
import auth from '../auth'

export default {
  methods: {
    toggleSidebar () {
      this.$store.commit('toggleSidebar')
    },
    logout () {
      return auth.logout()
    }
  },
  computed: {
    isAuthed () {
      return this.$store.state.user.isAuthed
    },
    username () {
      return this.$store.state.user.username
    }
  }
}
</script>

