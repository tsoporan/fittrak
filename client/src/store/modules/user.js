import * as types from '../mutation-types'

const state = {
  authed: false,
  username: '',
  email: ''
}

const getters = {
  user: state => {
    return { username: state.username, email: state.email, authed: state.authed }
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
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
