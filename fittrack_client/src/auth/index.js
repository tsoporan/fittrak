import Vue from 'vue'
import router from '../router'
import store from '../store'

const API_BASE = 'http://localhost:8000'
const LOGIN_URL = API_BASE + '/api-token-auth/'
const VERIFY_URL = API_BASE + '/api-token-verify/'

export default {
  user () {
    return store.state.user
  },

  isLoggedIn () {
    return this.user().authed
  },

  getToken () {
    return window.localStorage.getItem('token')
  },

  setToken (id) {
    window.localStorage.setItem('token', id)
  },

  removeToken () {
    window.localStorage.removeItem('token')
  },

  login (email, password, context) {
    let data = {
      username: email,
      password: password
    }

    return Vue.http.post(LOGIN_URL, data).then((res) => {
      // Success logging in
      let resData = res.body

      this.setToken(resData.token)

      store.commit('setAuthed', { authed: true, username: this.email })
      store.commit('setUser', {
        username: resData.username,
        email: resData.email
      })

      router.push({ path: '/home' })
    }, (res) => {
      // Failed login
      let errors = res.body

      context.$set.errors.username = errors.username
      context.$set.errors.password = errors.password
      context.$set.errors.formErrors = errors.non_field_errors[0]
    })
  },

  register () {
    console.log('do register')
  },

  logout () {
    this.removeToken()
    store.commit('setAuthed', { authed: false })
    router.push({ path: '/' })
  },

  checkAuth () {
    // Verifies that the current token is still usable
    console.log('checking auth')

    let token = this.getToken()
    let data = { token: token }

    return Vue.http.post(VERIFY_URL, data).then((res) => {
      console.log('*** verify token success')
      let data = res.body.user
      store.commit('setAuthed', { authed: true })
      store.commit('setUser', {
        username: data.username,
        email: data.email
      })
    }, (res) => {
      console.log('*** verify token failed')
      // Verification failed a new token will be required
      this.removeToken()
      this.reject()
    })
  }
}