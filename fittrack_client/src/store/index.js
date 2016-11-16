// Assemble modules and export store

import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import sidebar from './modules/sidebar'
import workouts from './modules/workouts'
import user from './modules/user'

Vue.use(Vuex) // Set up Vuex

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  actions,
  getters,
  modules: {
    user,
    sidebar,
    workouts
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
