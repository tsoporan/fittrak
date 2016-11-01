import Vue from 'vue'
import router from '../router'
import store from '../store'

const BASE_URL = 'http://localhost:8000/'
const LOGIN_URL = BASE_URL + 'api-token-auth/'
const VERIFY_URL = BASE_URL + 'api-token-verify/'

export default {
  isLoggedIn () {
    return store.state.users.isAuthed
  },

  login (email, password, context) {
    let data = {
      username: email,
      password: password
    }

    return Vue.http.post(LOGIN_URL, data).then((res) => {
      // Success logging in
      let resData = res.body

      window.localStorage.setItem('token', resData.token)

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
    window.localStorage.removeItem('token')
    store.commit('setAuthed', { authed: false })
    router.push({ path: '/' })
  },

  checkAuth () {
    // Verifies that the current token is still usable
    console.log('checking auth')

    let token = window.localStorage.getItem('token')

    return Vue.http.post(VERIFY_URL, { token: token }).then((res) => {
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
      window.localStorage.removeItem('token')
      this.reject()
    })
  }
}
