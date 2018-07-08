<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/history">History</router-link> |
    <router-link to="/settings">Settings</router-link> |
    <router-link to="/accounts/logout/">Sign out</router-link>
  </nav>
</template>

<script>
export default {
  name: "Navigation"
};
</script>
