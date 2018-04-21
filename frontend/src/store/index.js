// Assemble modules and export store

import Vue from 'vue'
import Vuex from 'vuex'
import meta from './modules/meta'
import user from './modules/user'
import workouts from './modules/workouts'

Vue.use(Vuex) // Set up Vuex

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    meta,
    user,
    workouts
  },
  strict: debug
})
