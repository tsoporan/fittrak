// Assemble modules and export store

import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import sidebar from './modules/sidebar'
import workouts from './modules/workouts'
import createLogger from '../../node_modules/vuex/src/plugins/logger'

Vue.use(Vuex) // Set up Vuex

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    user,
    sidebar,
    workouts
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
