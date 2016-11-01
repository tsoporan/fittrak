<template>
<div class="sidebar" v-bind:class="showSidebar">
  <div class="toggle-menu" v-on:click="toggleSidebar">
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
        <a href="">
          <span class="icon is-small"><i class="fa fa-heart" aria-hidden="true"></i></span>
          Track 
        </a>
      </li>

      <li>
        <a href="">
          <span class="icon is-small"><i class="fa fa-pie-chart" aria-hidden="true"></i></span>
          Progress
        </a>
      </li>

      <li>
        <a href="">
          <span class="icon is-small"><i class="fa fa-history" aria-hidden="true"></i></span>
          History
        </a>
      </li>

      <li>
        <a href="">
          <span class="icon is-small"><i class="fa fa-sliders" aria-hidden="true"></i></span>
          Settings
        </a>
      </li>

      <li>
        <a href="">
          <span class="icon is-small"><i class="fa fa-sign-out" aria-hidden="true"></i></span>
          Logout
        </a>
      </li>

    </ul>
  </aside>
</div>

</template>

<style lang="scss" scoped>
$darkgrey: #353535;
$darkgrey2: #444444;
$white: #ffffff;

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

div.sidebar.active {
  width: 20%;
  display: block;
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
</style>

<script>
export default {
  methods: {
    toggleSidebar () {
      this.$store.commit('toggleSidebar')
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


