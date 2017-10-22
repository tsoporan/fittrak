<template>
<div id="app" @click="away">
  <div class="container is-fluid">
    <Topbar></Topbar>
    <Sidebar></Sidebar>

    <div class="columns main">
      <div class="column">
        <router-view></router-view>
      </div>
    </div>
  </div> <!-- end container -->
</div>
</template>

<style lang="scss">
@import '../node_modules/bulma/css/bulma';
@import '../node_modules/font-awesome/scss/font-awesome';

div.main{
  margin-top: 3rem;
}

div.main h2 {
  margin: 0 1rem;
  text-align: center;
  font-size: 2rem;
}

form {
  padding: 1rem;
  margin: 1rem;
  background: white;
}

form label {
  display: block;
}

form input[type=submit] {
  display: block;
}
</style>


<script>
import Topbar from './components/Topbar'
import Sidebar from './components/Sidebar'

export default {
  methods: {
    away (e) {
      let clsName = e.target.className
      let showing = this.$store.getters.showSidebar

      // Close sidebar if clicked outside
      if (showing) {
        if (clsName !== 'sidebar active' && clsName !== 'fa fa-bars toggle-icon') {
          this.$store.dispatch('toggleSidebar')
        }
      }
    }
  },
  components: {
    Topbar,
    Sidebar
  }
}
</script>
