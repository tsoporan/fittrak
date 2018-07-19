<template>

<nav class="navbar is-primary" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://fittrak.ca">
      <h1 id="logo">FitTrak</h1>
    </a>

    <a role="button" class="navbar-burger" data-target="navMenu" aria-label="menu" aria-expanded="false">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div class="navbar-menu" id="navMenu">
    <div class="navbar-start">
      <router-link to="/" class="navbar-item">Home</router-link>
      <router-link to="/history" class="navbar-item">History</router-link>
      <router-link to="/settings" class="navbar-item">Settings</router-link>
    </div>

    <div class="navbar-end">
    <div class="navbar-item has-dropdown is-hoverable">
      <a class="navbar-link">
        <div>Heya, <strong>{{ username }}</strong></div>
      </a>
      <div class="navbar-dropdown">
        <a href="/accounts/logout/" class="navbar-item">
          Sign out
        </a>
        <hr class="navbar-divider">
        <a href="https://github.com/tsoporan/fittrak/releases" class="navbar-item">
          Release Notes
        </a>
      </div>
    </div>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: "Navigation",
  data() {
    return {
      username: "tsoporan"
    };
  }
};
</script>
