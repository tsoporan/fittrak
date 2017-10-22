import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    showSidebar: false,
    user: {
      authed: false,
      username: ''
    },
    workouts: {
      current: [],
      latest: []
    }
  },

  mutations: {
    toggleSidebar (state) {
      state.showSidebar = !state.showSidebar
    },

    setAuthed (state, payload) {
      state.user.authed = payload.authed
    },

    setUser (state, payload) {
      state.user.username = payload.username
      state.user.email = payload.email
    },

    setLatestWorkouts (state, payload) {
      state.workouts.latest = payload.latest
    }
  }
})

export default store
