<template>
<div class="sidebar" v-bind:class="showSidebar">
  <div class="toggle-menu" @click.prevent="toggleSidebar">
    <h1>
      <button>
        <span class="icon is-medium"><i class="fa fa-bars"></i></span>
      </button>
      <router-link to="/">FitTrack</router-link>
    </h1>
  </div>

  <aside class="menu">
    <p class="menu-label">Menu</p>
    <ul class="menu-list">
      <li>
        <router-link to="/home">
          <span class="icon is-small"><i class="fa fa-heart" aria-hidden="true"></i></span>
          Track 
        </router-link>
      </li>

      <li>
        <router-link to="/progress">
          <span class="icon is-small"><i class="fa fa-pie-chart" aria-hidden="true"></i></span>
          Progress
        </router-link>
      </li>

      <li>
        <router-link to="/history">
          <span class="icon is-small"><i class="fa fa-history" aria-hidden="true"></i></span>
          History
        </router-link>
      </li>

      <li>
        <router-link to="/settings">
          <span class="icon is-small"><i class="fa fa-sliders" aria-hidden="true"></i></span>
          Settings
        </router-link>
      </li>

      <li>
        <a href="" @click.prevent="logout">
          <span class="icon is-small"><i class="fa fa-sign-out" aria-hidden="true"></i></span>
          Logout
        </a>
      </li>

    </ul>
  </aside>

  <div class="sidebar-footer">
    <p>Made with <span style="color:red;">&#10084;</span> by <a href="https://github.com/tsoporan/fittrack">tsoporan</a></p>
  </div>
</div>

</template>

<style lang="scss" scoped>
@import '../../node_modules/bulma/sass/utilities/mixins';

$darkgrey: #353535;
$darkgrey2: #444444;
$darkgrey3: #2b2b2b;
$white: #ffffff;
$lightgrey: #c5c5c5;

div.sidebar-footer {
  bottom: 10px;
  position: absolute;
  text-align: center;
  width: 100%;
}

div.sidebar {
  z-index: 2;
  left: 0;
  top: 0;
  height: 100%;
  background: $darkgrey;
  position: fixed;
  color: $white;
  display: none;
}

div.sidebar.active {
  display: block;
  width: 50%;
}

@media (min-width: $tablet) {
  div.sidebar.active {
    width: 30%;
    display: block;
  }
}

@media (min-width: $desktop) {
  div.sidebar.active {
    width: 20%;
    display: block;
  }
}

div.sidebar h1 {
  color: $white;
  font-family: 'Kaushan Script', cursive;
  padding: 0;
}

div.sidebar h1 a {
  font-size: 2rem;
  display: inline-block;
  vertical-align: middle;
  color: $white;
}

div.sidebar h1 button {
  display: inline-block;
  vertical-align: middle;
  border: none;
}


div.sidebar aside.menu {
  padding: 1rem;
}

div.toggle-menu {
  border-bottom: 1px solid $darkgrey2;
}

div.toggle-menu button {
  background: $darkgrey;
  color: #fff;
  border: none;
}

div.toggle-menu button span {
  color: $white;
}

ul.menu-list a {
  color: $lightgrey;
}

ul.menu-list a:hover {
  background-color: $darkgrey3;
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
      this.$store.commit('toggleSidebar')
      return auth.logout()
    }
  },
  computed: {
    showSidebar () {
      return {
        active: this.$store.state.showSidebar
      }
    }
  }
}
</script>


