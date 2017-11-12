/*
 * API Helpers
 */

import Vue from 'vue'
import auth from './auth'
import Config from './config'

export default {
  get authHeaders () {
    return {
      headers: { Authorization: 'JWT ' + auth.getToken() }
    }
  },

  getRecentWorkouts: function () {
    return Vue.http.get(`${Config.API_BASE}/workouts/`, this.authHeaders)
  }
}
