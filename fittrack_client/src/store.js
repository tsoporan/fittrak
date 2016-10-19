import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    showSidebar: false
  },
  mutations: {
    toggleSidebar (state) {
      state.showSidebar = !state.showSidebar
    }
  }
})

export default store
