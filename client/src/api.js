/*
 * API Helpers
 */

import Vue from 'vue'
import auth from './auth'
import Config from './config'

export default {
  get: (path) => {
    return Vue.http.get(
      `${Config.API_BASE}${path}`,
      {
        headers: { Authorization: 'JWT ' + auth.getToken() }
      }
    )
  },
  post: (path, data) => {
    console.log('*** post', path, data)
  }
}
