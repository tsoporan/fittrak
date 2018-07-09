<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/history">History</router-link> |
    <router-link to="/settings">Settings</router-link> |
    <a href="/accounts/logout/">Sign out</a>
  </nav>
</template>

<script>
export default {
  name: "Navigation"
};
</script>
