<template>
<div id="app">
    <div class="container is-fluid">
        <Header></Header>
        <Sidebar></Sidebar>

        <div class="columns main">
            <div class="column"> 
            </div>
        </div>

        <Footer></Footer>
    </div> <!-- end container -->
</div>
</template>


<style lang="scss">
    @import './static/base';
</style>


<script>
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Footer from './components/Footer'

export default {
  data () {
    return {}
  },
  components: {
    Header,
    Sidebar,
    Footer
  }
}
</script>
