<template>
<div id="app">
    <div class="container is-fluid">
        <Topbar></Topbar>
        <Sidebar></Sidebar>

        <div class="columns main">
          <div class="column">
            <router-view></router-view>
          </div>
        </div>

        <Footer></Footer>
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
  components: {
    Topbar,
    Sidebar
  }
}
</script>
