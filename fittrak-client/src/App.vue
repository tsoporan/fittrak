<template>
  <div id="app">

    <Navigation />

    <div class="container">
      <div class="content-wrap">
        <router-view />
      </div>
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
div.content-wrap {
  margin: 10px;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
}
h2 {
  font-size: 20px;
}
div.page-content {
  padding: 5px;
}
h2.page-header {
  text-align: center;
  padding: 10px 0 0;
}
</style>
