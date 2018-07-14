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
export default {
  name: "App"
};
</script>
