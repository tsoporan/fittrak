import * as types from '../mutation-types'

const state = {
  authed: false,
  username: '',
  email: '',
  errors: {
    loginErrors: {
      username: '',
      password: '',
      form: ''
    },
    registrationErrors: {
      username: '',
      email: '',
      password: '',
      form: ''
    }
  }
}

const getters = {
  user: state => {
    return { username: state.username, email: state.email, authed: state.authed }
  },

  loginErrors: state => {
    return state.errors.loginErrors
  },

  registrationErrors: state => {
    return state.errors.registrationErrors
  }
}

const actions = {
  loginUser ({ commit, state }, payload) {
    commit(types.LOGIN_USER, payload)
  },

  logoutUser ({ commit, state }, payload) {
    commit(types.LOGOUT_USER, payload)
  },

  updateUser ({ commit, state }, payload) {
    commit(types.UPDATE_USER, payload)
  },

  setLoginErrors ({ commit, state }, payload) {
    commit(types.SET_LOGIN_ERRORS, payload)
  },

  setRegistrationErrors ({ commit, state }, payload) {
    commit(types.SET_REGISTRATION_ERRORS, payload)
  }
}

const mutations = {
  [types.LOGIN_USER] (state, payload) {
    state.authed = payload.authed
    state.username = payload.username
    state.email = payload.email
  },

  [types.LOGOUT_USER] (state, payload) {
    state.authed = payload.authed
  },

  [types.UPDATE_USER] (state, payload) {
    state.authed = payload.authed
    state.username = payload.username
    state.email = payload.email
  },

  [types.SET_LOGIN_ERRORS] (state, payload) {
    state.errors.loginErrors = payload.loginErrors
  },

  [types.SET_REGISTRATION_ERRORS] (state, payload) {
    state.errors.registrationErrors = payload.registrationErrors
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
