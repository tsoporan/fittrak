import Vue from 'vue'
import router from '../router'
import store from '../store'

import Config from '../config'

export default {
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
    const data = {
      username: email,
      password: password
    }

    return Vue.http.post(Config.LOGIN_URL, data).then((res) => {
      // Success logging in
      let resData = res.body

      this.setToken(resData.token)

      store.dispatch('loginUser', {
        username: resData.username,
        email: resData.email
      })

      router.push({ path: '/home' })
    })
  },

  register (username, email, password) {
    let data = {
      username: username,
      email: email,
      password1: password, // API Requires both passwords but we only capture password once
      password2: password
    }

    return Vue.http.post(Config.REGISTER_URL, data).then((res) => {
      // Sucessful registration
      let resData = res.body

      this.setToken(resData.token)

      // Login a user after successful registration
      store.dispatch('loginUser', {
        authed: true,
        username: resData.username,
        email: resData.email
      })

      router.push({ path: '/home' })
    })
  },

  logout () {
    this.removeToken()
    store.dispatch('logoutUser', { authed: false })
    router.push({ path: '/' })
  },

  emailVerification (emailVerifyKey) {
    let data = {
      key: emailVerifyKey
    }

    return Vue.http.post(Config.EMAIL_VERIFY_URL, data).then((res) => {
      router.push({ path: '/home' })
    }, (res) => {
      // TODO: Deal with error.
      console.log('Error')
      console.log(res.body)
    })
  },

  checkAuth () {
    // Verifies that the current token is still "good":  https://getblimp.github.io/django-rest-framework-jwt/#verify-token
    const token = this.getToken()

    return Vue.http.post(Config.VERIFY_URL, { token }).then((res) => {
      const { user } = res.body

      store.dispatch('updateUser', {
        username: user.username,
        email: user.email
      })
    }, (res) => {
      console.log('*** verify token failed', res)
      // Verification failed a new token will be required
      this.removeToken()
      this.reject()
    })
  }
}
