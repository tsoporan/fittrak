import * as types from '../mutation-types'

const state = {
  initialFetch: false,
  meta: false
}

const getters = {
  initialFetch: state => state.initialFetch
}

const actions = {
  refreshData ({ commit, state }, payload) {
    commit(types.REFRESH_DATA, payload)
  }
}

const mutations = {
  [types.REFRESH_DATA] (state, payload) {
    state.initialFetch = true
    state.meta = payload.meta
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
