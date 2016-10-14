<template>
<header>
<div class="columns is-mobile">
    <div class="column is-half">
    <h1><a href="#">FitTrack</a></h1>
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

header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  background: $white;
  padding: .1rem;
}

header h1 {
  font-size: 2rem;
  padding: 0 1rem;
  color: $white;
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
  data () {
    return {}
  }
}
</script>

