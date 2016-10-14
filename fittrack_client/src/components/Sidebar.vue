<template>
<div class="sidebar">
  <div class="toggle-menu">
      <button v-on:click="toggleMenu" v-bind:class="{ active: showMenu }">
      <span class="icon is-medium"><i class="fa fa-bars"></i></span>
    </button>
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
$white: #fffff;

div.sidebar {
  z-index: 2;
  left: 0;
  top: 0;
  width: 50%;
  height: 100%;
  background: $darkgrey;
  position: fixed;
  color: $white;
}

div.sidebar aside.menu {
  padding: 1rem;
}

div.sidebar div.toggle-menu {
  border-bottom: 1px solid $darkgrey2;
}

div.sidebar div.toggle-menu button span {
  color: $white;
}
</style>

<script>
export default {
  data () {
    return {
      showMenu: false
    }
  },
  methods: {
    toggleMenu: function () {
      this.showMenu = !this.showMenu
    }
  }
}
</script>


