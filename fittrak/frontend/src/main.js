// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import Vuetify from 'vuetify'

import App from './components/App'
import store from './store'
import router from './router'

Vue.use(Vuetify)
Vue.use(VueResource)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store,
  router,
  template: '<App/>',
  components: { App }
})
