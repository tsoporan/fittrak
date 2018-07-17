<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/history">History</router-link> |
      <router-link to="/settings">Settings</router-link> |
      <a href="/accounts/logout/">Sign out</a>
    </nav>

    <router-view />
  </div>
</template>

<script>
import "./../node_modules/bulma/css/bulma.css";

export default {
  name: "App"
};
</script>
