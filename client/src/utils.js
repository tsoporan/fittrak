// Routinely used methods.
import Vue from 'vue'
import auth from './auth'

const API_BASE = 'http://localhost:8000'

export default {
  getData (path) {
    let endpoint = API_BASE + path
    return Vue.http.get(
      endpoint,
      {
        headers: { Authorization: 'JWT ' + auth.getToken() }
      }
    )
  }
}
