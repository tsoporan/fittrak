<template>
  <div id="app">

    <Navigation />

    <div class="container">
      <router-view />
    </div>

  </div>
</template>

<script>
import "./../node_modules/bulma/css/bulma.css";

import Navigation from "@/components/Navigation";

export default {
  name: "App",
  components: {
    Navigation
  }
};
</script>

<style>
html,
body {
  width: 100%;
  height: 100%;
  background: #e7e7e7;
}
</style>
