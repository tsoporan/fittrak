import Vue from 'vue'
import App from '@/components/App'

describe('App.vue', () => {
  it('should render without crashing', () => {
    const Constructor = Vue.extend(App)
    new Constructor().$mount()
  })
})
