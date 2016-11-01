import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    showSidebar: false,
    user: {
      isAuthed: false,
      username: ''
    }
  },

  mutations: {
    toggleSidebar (state) {
      state.showSidebar = !state.showSidebar
    },

    setAuthed (state, payload) {
      state.user.isAuthed = payload.authed
    },

    setUser (state, payload) {
      state.user.username = payload.username
      state.user.email = payload.email
    }
  }
})

export default store
