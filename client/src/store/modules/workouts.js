import * as types from '../mutation-types'
import moment from 'moment'
import uuid from 'uuid/v4'

const state = {
  latest: [
    {
      started: moment().subtract(45, 'minutes'),
      ended: moment().subtract(5, 'minutes'),
      id: uuid()
    },
    {
      started: moment().subtract(5, 'hours'),
      ended: moment().subtract(4, 'hours'),
      id: uuid()
    },
    {
      started: moment().subtract(1, 'days'),
      ended: moment().subtract(1, 'days').add(30, 'minutes'),
      id: uuid()
    }
  ]
}

const getters = {}

const actions = {
  setLatestWorkouts ({ commit, state }, payload) {
    commit(types.SET_LATEST_WORKOUTS, payload)
  }
}

const mutations = {
  [types.SET_LATEST_WORKOUTS] (state, payload) {
    state.latest = state.latest.concat(payload.latest)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
