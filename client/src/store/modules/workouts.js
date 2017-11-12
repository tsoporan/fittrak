import * as types from '../mutation-types'

const state = {
  current: [],
  recent: []
}

const getters = {}

const actions = {
  setRecentWorkouts ({ commit, state }, payload) {
    commit(types.SET_RECENT_WORKOUTS, payload)
  }
}

const mutations = {
  [types.SET_RECENT_WORKOUTS] (state, payload) {
    state.recent = state.recent.concat(payload.workouts)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
