import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    showSidebar: false,
    user: {
      authed: false,
      username: '',
      email: ''
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

    setLatestWorkouts (state, payload) {
      state.workouts.latest = payload.latest
    }
  }
})

export default store
