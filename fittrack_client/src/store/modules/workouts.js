import * as types from '../mutation-types'

const state = {
  latest: [],
  current: []
}

const getters = {
  latestWorkouts: state => {
    return state.latest
  }
}

const actions = {
  setLatestWorkouts ({ commit, state }, payload) {
    commit(types.SET_LATEST_WORKOUTS, payload)
  }
}

const mutations = {
  [types.SET_LATEST_WORKOUTS] (state, payload) {
    state.latest.push(payload)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
