<template>
<header>
<div class="columns is-mobile">
    <div class="column is-half">
    <h1>
      <span class="icon is-medium" v-on:click="toggleSidebar">
        <i class="fa fa-bars"></i>
      </span>
      <a href="#">FitTrack</a>
    </h1>
    </div>

    <div class="column">
    <div class="profile-menu">
        <!-- <a class="button is-link" href="">{{ user.username }}</a> -->
        <a class="button is-secondary" href="#">Login</a>
        <a class="button is-secondary" href="#">Register</a>
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
  font-size: 2rem;
  padding: 0 1rem;
  color: $white;
}

header h1 a {
  display: inline-block;
  vertical-align: middle;
}

header h1 span.icon {
  color: $darkgrey;
  display: inline-block;
  vertical-align: middle;
}

div.profile-menu {
  text-align: right;
  margin-right: 1rem;
  margin-top: .3rem;
  color: $white;
}

</style>

<script>
export default {
  methods: {
    toggleSidebar () {
      this.$store.commit('toggleSidebar')
    }
  }
}
</script>

