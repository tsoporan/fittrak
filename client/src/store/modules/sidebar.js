import * as types from '../mutation-types'

const state = {
  showSidebar: false
}

const getters = {
  showSidebar: state => {
    return state.showSidebar
  }
}

const actions = {
  toggleSidebar ({ commit, state }) {
    commit(types.TOGGLE_SIDEBAR)
  }
}

const mutations = {
  [types.TOGGLE_SIDEBAR] (state) {
    state.showSidebar = !state.showSidebar
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
