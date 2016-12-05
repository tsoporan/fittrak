import Vue from 'vue'
import router from '../router'
import store from '../store'

const API_BASE = 'http://localhost:8000'
const LOGIN_URL = API_BASE + '/api-token-auth/'
const VERIFY_URL = API_BASE + '/api-token-verify/'
const REGISTER_URL = API_BASE + '/accounts/register'

export default {
  user () {
    let user = store.getters.user
    return user
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

  login (email, password) {
    let data = {
      username: email,
      password: password
    }

    return Vue.http.post(LOGIN_URL, data).then((res) => {
      // Success logging in
      let resData = res.body

      this.setToken(resData.token)

      store.dispatch('setAuthed', {
        authed: true
      })

      store.dispatch('setUser', {
        username: resData.username,
        email: resData.email
      })

      router.push({ path: '/home' })
    }, (res) => {
      // Failed login
      let errors = res.body

      store.dispatch('setLoginErrors', {
        loginErrors: {
          username: errors.username,
          password: errors.password,
          form: errors.non_field_errors[0]
        }
      })
    })
  },

  register (username, email, password) {
    let data = {
      username: username,
      email: email,
      password: password
    }

    return Vue.http.post(REGISTER_URL, data).then((res) => {
      console.log(res)
    }, (res) => {
      console.log(res)
    })
  },

  logout () {
    this.removeToken()
    store.dispatch('setAuthed', { authed: false })
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
      store.dispatch('setAuthed', { authed: true })
      store.dispatch('setUser', {
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
