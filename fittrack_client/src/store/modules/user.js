import * as types from '../mutation-types'

const state = {
  authed : false,
  username : ''
}

const getters = {
  user: state => {
    return { username: username, authed: authed }
  }
}

const actions = {
  setUser ({ commit, state }, payload) {
    commit(types.SET_USER, payload)
  },
  setAuthed ({ commit, state}, payload) {
    commit(types.SET_AUTHED, payload)
  }
}

const mutations = {
  [types.SET_USER] (state, payload) {
    state.username = payload.username
    state.authed = payload.authed
  },
  [types.SET_AUTHED] (state, payload) {
    state.authed = payload.authed
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
