import * as types from '../mutation-types'

const state = {
  authed: false,
  username: '',
  email: ''
}

const getters = {
  user: state => {
    return { username: state.username, authed: state.authed }
  }
}

const actions = {
  setUser ({ commit, state }, payload) {
    commit(types.SET_USER, payload)
  },

  setAuthed ({ commit, state }, payload) {
    commit(types.SET_AUTHED, payload)
  }
}

const mutations = {
  [types.SET_USER] (state, payload) {
    console.log('mutatation set user', state, payload)

    state.username = payload.username
    state.email = payload.email
  },

  [types.SET_AUTHED] (state, payload) {
    console.log('mutation set authed', payload.authed)
    state.authed = payload.authed
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
