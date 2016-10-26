import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/*', component: Home }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

export default router
