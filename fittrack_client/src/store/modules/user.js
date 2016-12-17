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
    return { username: state.username, authed: state.authed }
  },

  loginErrors: state => {
    return state.errors.loginErrors
  },

  registrationErrors: state => {
    return state.errors.registrationErrors
  }
}

const actions = {
  setUser ({ commit, state }, payload) {
    commit(types.SET_USER, payload)
  },

  setAuthed ({ commit, state }, payload) {
    commit(types.SET_AUTHED, payload)
  },

  setLoginErrors ({ commit, state }, payload) {
    commit(types.SET_LOGIN_ERRORS, payload)
  },

  setRegistrationErrors ({ commit, state }, payload) {
    commit(types.SET_REGISTRATION_ERRORS, payload)
  }
}

const mutations = {
  [types.SET_USER] (state, payload) {
    state.username = payload.username
    state.email = payload.email
  },

  [types.SET_AUTHED] (state, payload) {
    state.authed = payload.authed
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
